# Tubes-Basis-Data

## Deskripsi
Database ini mengimplementasikan sistem manajemen Formula 1 dengan schema lengkap mencakup data negara, tim, pembalap, grand prix, dan berbagai relasi yang terjalin.

## Struktur Database
Database **FormulaNone** mencakup tabel-tabel berikut:

### Tabel Utama
- **Negara** - Data negara
- **Tim** - Data tim Formula 1 dengan anggaran
- **Pembalap** - Data pembalap dengan nomor balap
- **GrandPrix** - Data grand prix/balapan
- **Sirkuit** - Data sirkuit/track
- **Musim** - Data musim Formula 1
- **Penghargaan** - Jenis penghargaan (POY, Pole, Fast Lap, dll)
- **Marshal** - Juri/marshal balapan
- **Supplier_Mesin** - Pemasok mesin

### Tabel Relasi
- **Kontrak** - Relasi pembalap dengan tim per musim
- **Memasok** - Relasi supplier dengan tim
- **Berpartisipasi_di** - Partisipasi pembalap di grand prix
- **Diberi_kepada** - Penghargaan diberikan ke pembalap
- **Mengawasi** - Marshal mengawasi sesi

## Cara Menjalankan

### Prerequisites
- Docker dan Docker Compose sudah terinstall
- Port 3307 tersedia (atau ubah di docker-compose.yml)

### Langkah-Langkah

1. **Clone/Navigasi ke folder project:**
   ```bash
   cd Tubes-Basis-Data
   ```

2. **Jalankan Docker Compose:**
   ```bash
   docker-compose up -d
   ```
   Atau dengan rebuild image:
   ```bash
   docker-compose up -d --build
   ```

3. **Tunggu container siap:**
   ```bash
   docker-compose logs -f mariadb
   ```
   Tunggu sampai muncul pesan "ready for connections"

4. **Container berjalan!**
   - Container name: `Tubes_Basdat`
   - Database: `FormulaNone`
   - User: `Tubes`
   - Password: `Tubes`
   - Port: `3307`

## 🔌 Akses Database

### Via MySQL Client
```bash
mysql -h 127.0.0.1 -P 3307 -u Tubes -p FormulaNone
# Password: Tubes
```

### Via DBeaver / MySQL Workbench
- Database: `FormulaNone`

### Via Docker Exec
```bash
docker exec -it Tubes_Basdat mysql -u Tubes -pTubes FormulaNone
```

## Menghentikan Container
```bash
docker-compose down
```

Untuk menghapus volume data juga:
```bash
docker-compose down -v
```

## Catatan
- Data akan persistent tersimpan di volume `mariadb_data`
- Container akan auto-restart jika crash (unless-stopped)
- Setiap kali container start, schema dan data awal akan di-load otomatis dari `db/FormulaNone.sql`