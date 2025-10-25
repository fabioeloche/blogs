#!/usr/bin/env python
"""
Script per aggiungere il campo external_url_image_link al database di produzione
"""
import os
import psycopg2
from urllib.parse import urlparse

# URL del database di produzione
DATABASE_URL = "postgresql://neondb_owner:npg_nmoZtluIy28j@ep-green-tree-a2e1ivdc.eu-central-1.aws.neon.tech/uncut_dried_trend_721081"

def add_field_to_production():
    """Aggiunge il campo external_url_image_link al database di produzione"""
    
    # Parse dell'URL del database
    url = urlparse(DATABASE_URL)
    
    try:
        # Connessione al database
        conn = psycopg2.connect(
            host=url.hostname,
            port=url.port,
            database=url.path[1:],  # Rimuove il '/' iniziale
            user=url.username,
            password=url.password
        )
        
        cursor = conn.cursor()
        
        # Comando SQL per aggiungere il campo
        sql_command = """
        ALTER TABLE blog_post 
        ADD COLUMN external_url_image_link VARCHAR(200) NULL;
        """
        
        print("Eseguendo comando SQL sul database di produzione...")
        cursor.execute(sql_command)
        conn.commit()
        
        print("✅ Campo 'external_url_image_link' aggiunto con successo!")
        
        # Verifica che il campo sia stato aggiunto
        cursor.execute("""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = 'blog_post' 
            AND column_name = 'external_url_image_link';
        """)
        
        result = cursor.fetchone()
        if result:
            print(f"✅ Verificato: Campo {result[0]} di tipo {result[1]} esiste nel database")
        else:
            print("❌ Errore: Campo non trovato")
            
    except psycopg2.errors.DuplicateColumn:
        print("ℹ️  Il campo 'external_url_image_link' esiste già nel database")
    except Exception as e:
        print(f"❌ Errore: {e}")
    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()
            print("🔌 Connessione chiusa")

if __name__ == "__main__":
    print("🚀 Aggiungendo campo al database di produzione Neon PostgreSQL...")
    add_field_to_production()
