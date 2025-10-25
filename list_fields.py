import psycopg2

# Connessione al database
conn = psycopg2.connect('postgresql://neondb_owner:npg_nmoZtluIy28j@ep-green-tree-a2e1ivdc.eu-central-1.aws.neon.tech/uncut_dried_trend_721081')
cursor = conn.cursor()

print("=== TUTTI I CAMPI DELLA TABELLA blog_post ===")
print(f"{'Campo':<30} {'Tipo':<25} {'Nullable'}")
print("-" * 70)

cursor.execute("""
    SELECT column_name, data_type, is_nullable 
    FROM information_schema.columns 
    WHERE table_name = 'blog_post' 
    ORDER BY ordinal_position;
""")

rows = cursor.fetchall()
for row in rows:
    print(f"{row[0]:<30} {row[1]:<25} {row[2]}")

cursor.close()
conn.close()
