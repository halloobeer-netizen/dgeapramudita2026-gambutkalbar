# PROJECT HANDOVER — APP SURVEY GAMBUT

## 1. Project Overview

**Project Name:** App Survey Gambut  
**Project Domain:** Survei lapangan gambut, data ekologis, koordinat, dokumentasi, QC, dan integrasi GIS  
**Status:** Existing Workflow / Application Specification Must Be Verified  
**Primary Context:** Survei gambut di Kalimantan Barat, termasuk pekerjaan Kapuas Hulu / KHG Kapuas-Bunut.

Project ini harus dianggap sebagai kelanjutan workflow survei yang sudah berjalan.

Detail stack aplikasi, repository, APK/web architecture, dan deployment **belum boleh ditebak**.  
AI/developer baru wajib memeriksa repository / source code aktual terlebih dahulu.

---

## 2. Core Objective

Aplikasi diarahkan untuk mendukung pencatatan data survei gambut di lapangan secara terstruktur.

Data utama mencakup:

- titik survei,
- surveyor,
- tanggal,
- koordinat,
- kondisi air,
- pH,
- EC,
- TDS,
- TMAT / TMAS,
- ketebalan gambut,
- tutupan lahan,
- vegetasi,
- substratum,
- kondisi genangan,
- status kawasan,
- tingkat kerusakan,
- dokumentasi,
- kebutuhan QC dan GIS.

---

## 3. Source of Truth

Untuk pengembangan selanjutnya, gunakan sumber berikut sebagai source of truth:

1. Repository aplikasi terbaru, jika tersedia.
2. Template survei terbaru.
3. MASTER GIS / QC terbaru.
4. Dataset koordinat aktual.
5. Ketentuan lapangan terbaru.
6. File foto dan dokumentasi yang terkait.

Jangan mengandalkan asumsi lama bila struktur field aktual pada file terbaru berbeda.

---

## 4. Important Survey Fields

Field survei yang sudah digunakan pada workflow mencakup:

```text
Nama Titik
Surveyor
Tanggal
Latitude
Longitude
Elevasi
TMAT
TMAS
pH
EC
TDS
Tutupan Lahan
Jenis Tanaman
Konsesi
Flora Fauna
Kerapatan Tajuk
Luapan / Genangan
Ketebalan Gambut
Kematangan Gambut
Karakteristik Substratum
Tingkat Kerusakan
```

Data pH / EC / TDS dapat memiliki kategori berbeda, antara lain:

```text
Air Tanah
Saluran
Substratum
```

Nama field aktual pada aplikasi harus mengikuti template / database terbaru.

---

## 5. Coordinate Standard

Koordinat survei menggunakan:

**WGS84 / EPSG:4326**

Konsep:

```text
Latitude = Y
Longitude = X
```

Pada template tertentu:

```text
Koord_Y → Latitude
Koord_X → Longitude
```

Jangan tertukar antara latitude dan longitude.

Gunakan format decimal degrees dengan titik (`.`), bukan koma, kecuali format ekspor tertentu memang membutuhkan format lokal.

---

## 6. GIS Direction

Data aplikasi harus mudah diekspor / digunakan untuk GIS.

Target kompatibilitas:

- CSV
- Excel
- GPX bila diperlukan
- GeoPackage
- Shapefile

Default coordinate reference:

```text
EPSG:4326
```

Untuk Shapefile:

- nama kolom idealnya tanpa spasi,
- perhatikan limit nama field,
- hindari struktur atribut yang sulit dibaca QGIS.

---

## 7. Survey Point Data

Workflow sebelumnya menggunakan banyak titik dengan kode seperti:

```text
TB-1.x
TB-2.x
TB-3.x
TB-4.x
```

Kode titik harus dipertahankan secara konsisten pada:

- database,
- foto,
- export,
- GIS,
- QC,
- nama folder.

Jangan membuat kode baru jika kode titik sudah diberikan.

---

## 8. Peat / Mineral Classification

Dalam workflow sebelumnya terdapat klasifikasi:

```text
GAMBUT
MINERAL
```

Pada proses dokumentasi tertentu digunakan rule berbasis jumlah foto:

```text
≥ 14 foto → gambut
< 14 foto → mineral
```

Rule ini berasal dari workflow klasifikasi dokumentasi tertentu.

Jangan secara otomatis menjadikannya scientific rule untuk seluruh aplikasi tanpa memeriksa business logic terbaru.

Jika aplikasi memiliki field klasifikasi gambut/mineral sendiri, gunakan field tersebut sebagai source of truth.

---

## 9. Peat Depth Classification

Dalam workflow sebelumnya digunakan kategori:

```text
Dangkal  = ≤ 3 m
Sedang   = 4–7 m
Dalam    = ≥ 8 m
```

Pada dokumentasi pengeboran:

```text
1 batang = 1 meter
```

Gunakan rule ini hanya bila masih sesuai dengan specification / template terbaru.

---

## 10. Field Quality Data

Data pengukuran yang sering digunakan:

- pH
- EC
- TDS

Contoh workflow sebelumnya memiliki pH sekitar:

```text
4.3 – 4.9
```

untuk sejumlah titik.

**Jangan menggunakan angka contoh sebagai default otomatis.**

Nilai pengukuran wajib berasal dari data alat / input lapangan yang sebenarnya.

---

## 11. Data Integrity

Aplikasi tidak boleh:

- membuat nilai pH secara acak,
- mengubah koordinat tanpa jejak,
- menebak kedalaman gambut,
- menebak TMAT/TMAS,
- mengisi data ilmiah yang kosong tanpa aturan eksplisit.

Field kosong harus tetap dianggap kosong / perlu verifikasi jika tidak ada sumber yang valid.

---

## 12. QC Workflow

QC data merupakan bagian penting.

Contoh issue yang harus bisa dideteksi:

```text
TMAT kosong
Kedalaman gambut kosong
Koordinat kosong
Koordinat tidak valid
Nama titik duplicate
Field wajib belum terisi
```

Ideal flow:

```text
Survey Input
     ↓
Validation
     ↓
Save
     ↓
QC Status
     ↓
Review
     ↓
Approved / Need Revision
```

Jika repository sudah memiliki workflow lain, pertahankan implementation aktual.

---

## 13. Recommended QC Status

Jika belum tersedia, konsep status:

```text
DRAFT
SUBMITTED
NEED_REVISION
VERIFIED
APPROVED
```

Tetapi jangan menambah enum baru sebelum mengecek schema yang sudah ada.

---

## 14. Documentation / Photo Direction

Dokumentasi lapangan merupakan bagian dari workflow.

Kategori foto yang pernah digunakan:

```text
Tutupan Lahan
pH / EC / TDS Mineral
Pengeboran Mineral
Mineral
Gambut
```

Contoh pola label:

```text
TB-xx tutupan lahan
TB-xx Ph/ec/tds mineral
TB-xx Pengeboran mineral
TB-xx mineral
```

Jika aplikasi mendukung upload foto, foto harus terhubung ke `Nama Titik` yang benar.

---

## 15. Photo-to-Point Consistency

Rule dokumentasi yang sudah pernah dikunci:

```text
Foto 1 → Koordinat 1
Foto 2 → Koordinat 2
Foto 3 → Koordinat 3
...
```

Konsep utama:

**SATU KOORDINAT → SATU FOTO**

untuk batch workflow yang menggunakan pasangan tersebut.

Jangan mengacak urutan foto dan koordinat.

---

## 16. Coordinate Variation for Photo Documentation

Pada workflow batch tertentu:

- titik foto dibuat dalam jarak kecil antar dokumentasi,
- kisaran yang pernah digunakan sekitar 1–2 m atau 1–3 m sesuai batch.

Jangan membuat variasi koordinat otomatis pada aplikasi production tanpa instruksi.

Jika GPS device tersedia, gunakan koordinat aktual.

---

## 17. Photo Editing Rules from Existing Workflow

Untuk workflow editing dokumentasi:

- teks koordinat diletakkan di bagian bawah,
- alamat dihapus,
- angka pada layar alat dipertahankan,
- hanya kode titik dan koordinat yang diganti ketika melakukan batch editing,
- font / ukuran / posisi harus konsisten.

Aplikasi tidak perlu meniru edit foto ini kecuali memang memiliki fitur watermark/export dokumentasi.

---

## 18. Watermark Direction

Pada dokumentasi lapangan sebelumnya pernah digunakan struktur watermark:

```text
Jam → kiri
Lokasi → kanan
Cuaca / suhu → bawah tengah
```

Contoh lokasi:

```text
Kapuas Hulu
Kalimantan Barat
```

Jika fitur watermark dikembangkan, gunakan konfigurasi fleksibel.

Jangan hard-code lokasi jika aplikasi akan digunakan untuk area lain.

---

## 19. Existing Data Scale

Workflow GIS sebelumnya mencakup dataset besar, termasuk dataset sekitar:

```text
1,073 titik GPX
```

Dalam proses pencocokan tertentu:

```text
440 titik cocok nama MASTER_GIS
633 titik merupakan estimasi berdasarkan referensi terdekat
```

Titik estimasi perlu verifikasi terhadap batas administrasi resmi.

Aplikasi harus membedakan data aktual vs data estimasi bila kedua jenis data digunakan.

---

## 20. Administrative Boundary Safety

Jangan menganggap desa/kecamatan hasil estimasi sebagai data final.

Jika titik berasal dari nearest-reference estimation:

```text
status = needs verification
```

atau mekanisme equivalent.

Untuk keputusan resmi, gunakan batas administrasi / sumber GIS yang valid.

---

## 21. Data Import

Aplikasi idealnya dapat menangani sumber seperti:

- Excel
- CSV
- GPX

Ketika import:

1. Preview data.
2. Validasi kolom.
3. Validasi koordinat.
4. Deteksi duplicate point.
5. Jangan overwrite data lama tanpa konfirmasi.
6. Beri laporan baris gagal.

---

## 22. Data Export

Export harus menjaga:

- Nama Titik
- koordinat
- surveyor
- tanggal
- seluruh parameter lapangan
- status QC
- klasifikasi
- relasi foto jika memungkinkan

Prioritas kompatibel dengan Excel dan QGIS.

---

## 23. Offline Field Consideration

Karena aplikasi digunakan untuk survey lapangan, desain harus mempertimbangkan kemungkinan koneksi internet buruk.

Jika architecture memungkinkan:

```text
Input locally
↓
Save draft
↓
Sync when network available
↓
Server confirmation
```

Namun jangan implementasikan ulang architecture offline sebelum mengecek repository saat ini.

---

## 24. Validation Rules

Minimum validation yang direkomendasikan:

### Latitude
```text
-90 to 90
```

### Longitude
```text
-180 to 180
```

### Nama Titik
Tidak boleh kosong.

### Numeric Measurement
Harus berupa angka valid atau `null`.

Jangan mengubah `null` menjadi `0` kecuali scientific/business rule memang menyatakan demikian.

---

## 25. Database Safety

Dilarang tanpa izin:

```text
DROP DATABASE
DROP TABLE
TRUNCATE
delete all survey points
bulk overwrite coordinates
reset verified QC data
```

Data lapangan merupakan data penting.

Gunakan migration dan audit trail bila schema berubah.

---

## 26. Recommended Data History

Untuk perubahan penting seperti:

- koordinat,
- ketebalan gambut,
- TMAT,
- klasifikasi,
- QC approval,

idealnya simpan:

```text
updatedAt
updatedBy
previous value / change log
```

Implementasikan hanya bila kompatibel dengan architecture existing.

---

## 27. Application Stack — MUST VERIFY

Belum ada dokumentasi yang cukup kuat untuk mengunci:

- framework frontend,
- backend framework,
- database,
- APK native / PWA / web,
- hosting,
- repository,
- authentication,
- sync implementation.

Karena itu:

**JANGAN MENGARANG STACK.**

Developer / AI baru harus memeriksa source code aktual.

---

## 28. Mandatory Takeover Audit

Sebelum coding, hasilkan:

```text
PROJECT AUDIT — APP SURVEY GAMBUT

1. Repository / project structure
2. Application type: APK / web / PWA / hybrid
3. Current frontend stack
4. Backend stack
5. Database
6. Authentication
7. Survey form structure
8. Existing fields
9. Coordinate handling
10. Photo handling
11. Offline capability
12. Sync mechanism
13. Import/export
14. QC workflow
15. GIS integration
16. Current working features
17. Broken/incomplete features
18. Deployment/build status
19. Data migration risks
20. Recommended next task
```

Baru setelah audit, lanjutkan development.

---

## 29. Main Development Priority

Urutan prioritas yang aman:

### Priority 1
Pastikan semua data survei existing aman.

### Priority 2
Audit form dan schema terhadap template terbaru.

### Priority 3
Pastikan koordinat benar.

### Priority 4
Pastikan foto terhubung ke titik yang benar.

### Priority 5
Validasi pH/EC/TDS/TMAT/TMAS/kedalaman.

### Priority 6
Sempurnakan QC.

### Priority 7
Sempurnakan import/export.

### Priority 8
Sempurnakan kompatibilitas GIS.

### Priority 9
Offline + synchronization jika dibutuhkan.

### Priority 10
Reporting / dashboard.

---

## 30. Locked / Preserved Principles

Pertahankan prinsip berikut:

- Nama titik harus konsisten.
- Koordinat menggunakan WGS84 / EPSG:4326 kecuali ada kebutuhan CRS lain.
- Latitude dan longitude tidak boleh tertukar.
- Data ilmiah tidak boleh dibuat-buat.
- Data kosong tidak boleh diam-diam diisi angka palsu.
- Foto harus terhubung ke titik yang benar.
- QC harus mampu menunjukkan data kurang / invalid.
- Data estimasi harus dibedakan dari data terverifikasi.
- Export harus tetap kompatibel dengan workflow Excel/QGIS.
- Jangan merusak data lama.
- Jangan rebuild project sebelum audit source code.

---

## 31. Correct Continuation Workflow

```text
READ SOURCE
↓
AUDIT
↓
BACKUP / PROTECT DATA
↓
COMPARE WITH LATEST SURVEY TEMPLATE
↓
VERIFY DATABASE FIELDS
↓
VERIFY COORDINATES
↓
VERIFY PHOTO LINKS
↓
VERIFY QC
↓
FIX
↓
TEST
↓
EXPORT TEST
↓
GIS TEST
↓
COMMIT / DEPLOY
```

Bukan:

```text
ASSUME
↓
REBUILD
↓
LOSE FIELD DATA
```

---

## 32. Final Instruction

This project contains field survey data that may be difficult or impossible to recreate.

Data integrity is more important than aggressive refactoring.

The next AI/developer must first understand the existing application and survey workflow, then continue incrementally while preserving verified field data, coordinates, photos, QC status, and GIS compatibility.
