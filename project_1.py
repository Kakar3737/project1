listPasien = [
    {
        'nama': 'Sugih',
        'usia': 20,
        'tgl': 'Yogyakarta, 20 Mei 2002',
        'terakhir' : '19 Januari 2020',
        'penyakit' : 'batuk'
    },
    {
        'nama': 'Djaja',
        'usia': 15,
        'tgl': 'Jakarta, 12 Januari 2007',
        'terakhir' : '20 Desember 2019',
        'penyakit' : 'diabetes'
    },
    {
        'nama': 'Tedy',
        'usia': 25,
        'tgl': 'Bandung, 2 Maret `1997',
        'terakhir' : '1 Februari 2020',
        'penyakit' : 'vertigo'
    }
]
# --------------------------------------------------------------------------------------------------------------------------------------


def menampilkanDaftarPasienMenu() :
  while True :
      pilihanMenu = input('''
        Menampilkan Data Pasien
        
        List Menu :
        1. Menampilkan Seluruh Daftar Pasien Rumah Sakit
        2. Menampilkan Data Pasien Tertentu
        3. Back to Menu

        Masukkan angka Menu yang ingin dijalankan : ''')
      if(pilihanMenu == '1') :
        menampilkanDaftarPasienAll()
      elif(pilihanMenu == '2') :
        menampilkanDaftarPasienSP()
      elif(pilihanMenu == '3') :
        break
      else:
        print('Input salah, coba lagi')

    
def menampilkanDaftarPasienAll() :
  if len(listPasien) == 0 :
    print('Daftar pasien kosong')
  else:
    print('Daftar Pasien Rumah Sakit\n')
    print('Index\t| Nama Pasien  \t| Usia\t| Tempat/Tanggal Lahir     \t| Kunjungan Terakhir  \t| Riwayat Penyakit')
    for i in range(len(listPasien)) :
        print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(i,listPasien[i]['nama'],listPasien[i]['usia'],listPasien[i]['tgl'],listPasien[i]['terakhir'],listPasien[i]['penyakit']))

def menampilkanDaftarPasienSP() :
  if len(listPasien) == 0 :
    print('Daftar pasien kosong')
  else:
    pilihPasien = int(input('''Masukkan Index Pasien yang Ingin Ditampilkan : '''))
    if(len(listPasien)>pilihPasien) :
      print('Index\t| Nama Pasien  \t| Usia\t| Tempat/Tanggal Lahir     \t| Kunjungan Terakhir \t| Riwayat Penyakit')
      print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(pilihPasien,listPasien[pilihPasien]['nama'],listPasien[pilihPasien]['usia'],listPasien[pilihPasien]['tgl'],listPasien[pilihPasien]['terakhir'],listPasien[pilihPasien]['penyakit']))
    else:
      print('Pasien belum terdaftar')

# --------------------------------------------------------------------------------------------------------------------------------------

def menambahPasienMenu() :
  while True :
      pilihanMenu = input('''
        Menambah Data Pasien Baru
        
        List Menu :
        1. Menambah Data Pasien Baru
        2. Back to Menu

        Masukkan angka Menu yang ingin dijalankan : ''')
      if(pilihanMenu == '1') :
        pilihPasien = int(input('''Masukkan Index Pasien yang Ingin Ditambahkan : '''))
        if(len(listPasien)>pilihPasien) :
          print('Pasien sudah terdaftar')
        else:
          namaPasien = input('Masukkan Nama Pasien Baru : ')
          Umur = int(input('Masukkan Usia : '))
          Tanggal = input('Masukkan Tempat/Tanggal Lahir : ')
          Terakhir = input('Masukkan Tanggal Kunjungan Terakhir : ')
          Penyakit = input('Masukkan Penyakit yang Diderita Pasien Saat Ini : ')
          while True :
            pilihanMenu = input('''
            Simpan Data ? :
            1. Ya
            2. Tidak

            Masukkan angka Pilihan yang ingin dijalankan : ''')
            if(pilihanMenu == '1') :
              listPasien.append({
              'nama': namaPasien,
              'usia': Umur,
              'tgl': Tanggal,
              'terakhir' : Terakhir,
              'penyakit' : Penyakit
            })
              print('Data Tersimpan')
              break
            elif(pilihanMenu == '2') :
              break
            else:
              print('Input salah, coba lagi')
      elif(pilihanMenu == '2') :
        break
      else:
        print('Input salah, coba lagi')

  

        
# --------------------------------------------------------------------------------------------------------------------------------------
def menghapusDataPasienMenu() :
    while True :
      pilihanMenu = input('''
        Menghapus Data Pasien
        
        List Menu :
        1. Menghapus Data Pasien
        2. Back to Menu

        Masukkan angka Menu yang ingin dijalankan : ''')
      if(pilihanMenu == '1') :
        menghapusDataPasien()
      elif(pilihanMenu == '2') :
        break
      else:
        print('Input salah, coba lagi')

def menghapusDataPasien() :
  pilihPasien = int(input('''Masukkan Index Pasien yang Ingin Dihapus : '''))
  if(len(listPasien)>pilihPasien) :
    while True :
      pilihanMenu = input('''
          Hapus Data ? :
          1. Ya
          2. Tidak

          Masukkan angka Pilihan yang ingin dijalankan : ''')
      if(pilihanMenu == '1') :
        del listPasien[pilihPasien]
        print('Data Dihapus')
        break
      elif(pilihanMenu == '2') :
        break
      else:
        print('Input salah, coba lagi')
  else:
    print('Pasien tidak terdaftar')
# --------------------------------------------------------------------------------------------------------------------------------------

def updateDataMenu() :
  while True :
      pilihanMenu = input('''
        Memperbarui Data Pasien
        
        List Menu :
        1. Memperbarui Data Pasien
        2. Back to Menu

        Masukkan angka Menu yang ingin dijalankan : ''')
      if(pilihanMenu == '1') :
        updateData()
      elif(pilihanMenu == '2') :
        break
      else:
        print('Input salah, coba lagi')

def updateData() :
  pilihPasien = int(input('''Masukkan Index Pasien yang Ingin Diganti : '''))
  if(len(listPasien)>pilihPasien) :
    print('Index\t| Nama Pasien  \t| Usia\t| Tempat/Tanggal Lahir     \t| Kunjungan Terakhir \t| Riwayat Penyakit')
    print('{}\t| {}  \t| {}\t| {}\t| {}\t| {}'.format(pilihPasien,listPasien[pilihPasien]['nama'],listPasien[pilihPasien]['usia'],listPasien[pilihPasien]['tgl'],listPasien[pilihPasien]['terakhir'],listPasien[pilihPasien]['penyakit']))
    while True :
      pilihanMenu = input('''
          Lanjut Update ? :
          1. Ya
          2. Tidak

          Masukkan angka Pilihan yang ingin dijalankan : ''')
      if(pilihanMenu == '1') :
        pilihKolom = input('''Masukkan kolom yang Ingin Diganti : ''')
        if(pilihKolom == 'Nama Pasien') :
          listPasien[pilihPasien]['nama'] = input('''Masukkan nama pasien : ''')
          print('Data berhasil diganti')
          break
        elif(pilihKolom == 'Usia') :
          listPasien[pilihPasien]['usia'] = input('''Masukkan usia pasien : ''')
          print('Data berhasil diganti')
          break
        elif(pilihKolom == 'Tempat/Tanggal Lahir'):
          listPasien[pilihPasien]['tgl'] =  input('''Masukkan tempat/tanggal lahir pasien : ''')
          print('Data berhasil diganti')
          break
        elif(pilihKolom == 'Kunjungan Terakhir'):
          listPasien[pilihPasien]['terakhir'] =  input('''Masukkan tanggal kunjungan terakhir : ''')
          print('Data berhasil diganti')
          break
        elif(pilihKolom == 'Riwayat Penyakit'):
          temp = input('''Masukkan penyakit yang diderita pasien saat ini : ''')
          listPasien[pilihPasien]['penyakit'] += ', ' +temp
          print('Data berhasil ditambahkan')
          break
        else:
          print('Input salah, coba lagi')
      elif(pilihanMenu == '2') :
        break
      else:
        print('Input salah, coba lagi')
  else:
    print('Pasien tidak terdaftar')

# --------------------------------------------------------------------------------------------------------------------------------------
while True :
    pilihanMenu = input('''
        Selamat Datang di Rumah Sakit

        List Menu :
        1. Menampilkan Daftar Pasien Rumah Sakit
        2. Menambah Data Pasien Baru
        3. Menghapus Data Pasien
        4. Memperbarui Data Pasien
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

    if(pilihanMenu == '1') :
        menampilkanDaftarPasienMenu()
    elif(pilihanMenu == '2') :
        menambahPasienMenu()
    elif(pilihanMenu == '3') :
        menghapusDataPasienMenu()
    elif(pilihanMenu == '4') :
        updateDataMenu()
    elif(pilihanMenu == '5') :
        break
    else:
        print('Input Salah, Coba lagi')