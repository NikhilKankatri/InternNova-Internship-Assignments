# Runs the SQL files on a SQLite database (company.db) and saves each query with its output.
import os, json, sqlite3

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, "company.db")
if os.path.exists(DB):
    os.remove(DB)
con = sqlite3.connect(DB)

def split_statements(text):
    """Split a .sql file into (comment_lines, statement) pairs."""
    out, buf, comments = [], "", []
    for line in text.split("\n"):
        if not buf and line.strip().startswith("--"):
            comments.append(line.strip()); continue
        if not buf and not line.strip():
            continue
        buf += line + "\n"
        if sqlite3.complete_statement(buf):
            out.append((comments, buf.strip())); buf, comments = "", []
    return out

def fmt(v):
    if v is None: return "NULL"
    if isinstance(v, float): return f"{v:.2f}".rstrip("0").rstrip(".") if v != int(v) else str(int(v))
    return str(v)

def table(cols, rows):
    rows = [[fmt(v) for v in r] for r in rows]
    w = [max(len(c), *(len(r[i]) for r in rows)) if rows else len(c) for i, c in enumerate(cols)]
    line = "+" + "+".join("-" * (x + 2) for x in w) + "+"
    def row(vals, num=False):
        return "| " + " | ".join(v.rjust(w[i]) if (num and v.replace('.','',1).replace('-','',1).isdigit()) else v.ljust(w[i])
                                for i, v in enumerate(vals)) + " |"
    res = [line, row(cols), line] + [row(r, True) for r in rows] + [line]
    res.append(f"{len(rows)} row{'s' if len(rows) != 1 else ''} in set")
    return "\n".join(res)

# database setup
con.executescript(open(os.path.join(BASE, "00_setup_database.sql")).read())
print("Database created: company.db")

files = ["task1_select", "task2_where_orderby_aggregates", "task3_groupby_having",
         "task4_joins", "task5_subqueries"]
for f in files:
    blocks = []
    for comments, stmt in split_statements(open(os.path.join(BASE, f + ".sql")).read()):
        cur = con.execute(stmt)
        cols = [d[0] for d in cur.description]
        blocks.append({"comment": comments[-1].lstrip("- ").strip() if comments else "",
                       "sql": stmt, "result": table(cols, cur.fetchall())})
    json.dump(blocks, open(os.path.join(BASE, "outputs", f + ".json"), "w"), indent=1)
    with open(os.path.join(BASE, "outputs", f + ".txt"), "w") as fh:
        for b in blocks:
            fh.write(f"-- {b['comment']}\nmysql> {b['sql']}\n{b['result']}\n\n")
    print(f, "->", len(blocks), "queries")
con.close()
