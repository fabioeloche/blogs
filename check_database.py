#!/usr/bin/env python
import psycopg2

# Connessione al database di produzione
DATABASE_URL = "postgresql://neondb_owner:npg_nmoZtluIy28j@ep-green-tree-a2e1ivdc.eu-central-1.aws.neon.tech/uncut_dried_trend_721081"

try:
    # Connessione
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    print("✅ Connesso al database di produzione!")
    print("\n=== STRUTTURA TABELLA blog_post ===")
    
    # Query per ottenere la struttura della tabella
    cursor.execute("""
        SELECT column_name, data_type, is_nullable 
        FROM information_schema.columns 
        WHERE table_name = 'blog_post' 
        ORDER BY ordinal_position;
    """)
    
    rows = cursor.fetchall()
    
    print(f"{'Campo':<30} {'Tipo':<20} {'Nullable'}")
    print("-" * 60)
    
    for row in rows:
        print(f"{row[0]:<30} {row[1]:<20} {row[2]}")
    
    # Verifica specifica del campo external_url_image_link
    cursor.execute("""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name = 'blog_post' 
        AND column_name = 'external_url_image_link';
    """)
    
    result = cursor.fetchone()
    if result:
        print(f"\n✅ Campo 'external_url_image_link' ESISTE nel database!")
    else:
        print(f"\n❌ Campo 'external_url_image_link' NON ESISTE nel database!")
        
except Exception as e:
    print(f"❌ Errore: {e}")
finally:
    if 'conn' in locals():
        cursor.close()
        conn.close()
        print("\n🔌 Connessione chiusa")
