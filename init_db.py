# init_db.py — buat tabel PostgreSQL (jalankan sekali)
from config.database import get_db

db = get_db()
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students (
  id          VARCHAR(36) PRIMARY KEY,
  nama        VARCHAR(100) NOT NULL,
  nim         VARCHAR(30)  NOT NULL UNIQUE,
  kelas       VARCHAR(50)  NOT NULL,
  prodi       VARCHAR(100) NOT NULL,
  photo       TEXT,
  descriptors TEXT         NOT NULL DEFAULT '[]',
  created_at  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS attendance (
  id          SERIAL PRIMARY KEY,
  student_id  VARCHAR(36)  NOT NULL,
  nama        VARCHAR(100) NOT NULL,
  nim         VARCHAR(30)  NOT NULL,
  kelas       VARCHAR(50)  NOT NULL,
  prodi       VARCHAR(100) NOT NULL,
  time        TIMESTAMP    NOT NULL,
  date        DATE         NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);
""")

cur.execute("CREATE INDEX IF NOT EXISTS idx_date ON attendance(date);")
cur.execute("CREATE INDEX IF NOT EXISTS idx_student ON attendance(student_id);")

db.commit()
cur.close()
db.close()
print("Tabel berhasil dibuat!")
