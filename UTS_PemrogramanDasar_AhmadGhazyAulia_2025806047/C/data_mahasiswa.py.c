#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ========== STRUCT ==========
typedef struct Mahasiswa {
    char nama[50];
    char nim[15];
    float tugas;
    float uts;
    float uas;
    float nilai_akhir;
    char mutu[3];
    struct Mahasiswa *next;
} Mahasiswa;

// ========== FUNGSI BANTU ==========
void hitung_nilai(Mahasiswa *m) {
    m->nilai_akhir = (m->tugas * 0.30f) + (m->uts * 0.30f) + (m->uas * 0.40f);

    if (m->nilai_akhir >= 80)      strcpy(m->mutu, "A");
    else if (m->nilai_akhir >= 70) strcpy(m->mutu, "B");
    else if (m->nilai_akhir >= 60) strcpy(m->mutu, "C");
    else if (m->nilai_akhir >= 50) strcpy(m->mutu, "D");
    else                           strcpy(m->mutu, "E");
}

// ========== ADD ==========
Mahasiswa* add(Mahasiswa *head, char *nama, char *nim, float tugas, float uts, float uas) {
    Mahasiswa *baru = (Mahasiswa*) malloc(sizeof(Mahasiswa));
    if (!baru) {
        printf("Alokasi memori gagal!\n");
        return head;
    }
    strncpy(baru->nama, nama, 49);
    strncpy(baru->nim,  nim,  14);
    baru->tugas = tugas;
    baru->uts   = uts;
    baru->uas   = uas;
    baru->next  = NULL;
    hitung_nilai(baru);

    if (!head) return baru;

    Mahasiswa *cur = head;
    while (cur->next) cur = cur->next;
    cur->next = baru;
    return head;
}

// ========== SEARCH ==========
Mahasiswa* search(Mahasiswa *head, char *nim) {
    Mahasiswa *cur = head;
    while (cur) {
        if (strcmp(cur->nim, nim) == 0) return cur;
        cur = cur->next;
    }
    return NULL;
}

// ========== DELETE ==========
Mahasiswa* delete_nim(Mahasiswa *head, char *nim) {
    if (!head) return NULL;

    if (strcmp(head->nim, nim) == 0) {
        Mahasiswa *tmp = head->next;
        printf("Mahasiswa '%s' (NIM: %s) berhasil dihapus.\n", head->nama, head->nim);
        free(head);
        return tmp;
    }

    Mahasiswa *cur = head;
    while (cur->next) {
        if (strcmp(cur->next->nim, nim) == 0) {
            Mahasiswa *tmp = cur->next;
            cur->next = tmp->next;
            printf("Mahasiswa '%s' (NIM: %s) berhasil dihapus.\n", tmp->nama, tmp->nim);
            free(tmp);
            return head;
        }
        cur = cur->next;
    }
    printf("NIM %s tidak ditemukan.\n", nim);
    return head;
}

// ========== PRINT ==========
void print_table(Mahasiswa *head) {
    printf("\n%-20s %-12s %6s %6s %6s %10s %5s\n",
           "Nama", "NIM", "Tugas", "UTS", "UAS", "NilaiAkhir", "Mutu");
    printf("%-20s %-12s %6s %6s %6s %10s %5s\n",
           "--------------------", "------------", "------", "------", "------", "----------", "-----");

    Mahasiswa *cur = head;
    while (cur) {
        printf("%-20s %-12s %6.1f %6.1f %6.1f %10.2f %5s\n",
               cur->nama, cur->nim, cur->tugas, cur->uts, cur->uas,
               cur->nilai_akhir, cur->mutu);
        cur = cur->next;
    }
    printf("\n");
}

// ========== SAVE CSV ==========
void save_csv(Mahasiswa *head, const char *filename) {
    FILE *f = fopen(filename, "w");
    if (!f) {
        printf("Gagal membuka file %s\n", filename);
        return;
    }
    fprintf(f, "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n");
    Mahasiswa *cur = head;
    while (cur) {
        fprintf(f, "%s,%s,%.1f,%.1f,%.1f,%.2f,%s\n",
                cur->nama, cur->nim, cur->tugas, cur->uts, cur->uas,
                cur->nilai_akhir, cur->mutu);
        cur = cur->next;
    }
    fclose(f);
    printf("Data berhasil disimpan ke %s\n", filename);
}

// ========== FREE ALL ==========
void free_all(Mahasiswa *head) {
    while (head) {
        Mahasiswa *tmp = head;
        head = head->next;
        free(tmp);
    }
}

// ========== BUBBLE SORT (bonus) ==========
Mahasiswa* bubble_sort(Mahasiswa *head) {
    if (!head || !head->next) return head;
    int swapped;
    do {
        swapped = 0;
        Mahasiswa *cur = head;
        while (cur->next) {
            if (cur->nilai_akhir < cur->next->nilai_akhir) {
                // swap data (bukan pointer)
                char tmp_nama[50], tmp_nim[15];
                float tmp_t, tmp_u, tmp_a, tmp_na;
                char tmp_m[3];

                strcpy(tmp_nama, cur->nama);   strcpy(cur->nama,       cur->next->nama);   strcpy(cur->next->nama,       tmp_nama);
                strcpy(tmp_nim,  cur->nim);    strcpy(cur->nim,        cur->next->nim);    strcpy(cur->next->nim,        tmp_nim);
                tmp_t = cur->tugas; cur->tugas = cur->next->tugas; cur->next->tugas = tmp_t;
                tmp_u = cur->uts;   cur->uts   = cur->next->uts;   cur->next->uts   = tmp_u;
                tmp_a = cur->uas;   cur->uas   = cur->next->uas;   cur->next->uas   = tmp_a;
                tmp_na= cur->nilai_akhir; cur->nilai_akhir = cur->next->nilai_akhir; cur->next->nilai_akhir = tmp_na;
                strcpy(tmp_m, cur->mutu); strcpy(cur->mutu, cur->next->mutu); strcpy(cur->next->mutu, tmp_m);
                swapped = 1;
            }
            cur = cur->next;
        }
    } while (swapped);
    return head;
}

// ========== MENU ==========
int main() {
    Mahasiswa *head = NULL;
    int pilihan;
    char nama[50], nim[15];
    float tugas, uts, uas;

    // Data contoh awal
    head = add(head, "Rina",  "2310001", 80, 85, 90);
    head = add(head, "Doni",  "2310002", 60, 55, 70);
    head = add(head, "Sari",  "2310003", 75, 78, 82);
    head = add(head, "Bagas", "2310004", 90, 88, 95);
    head = add(head, "Dewi",  "2310005", 55, 60, 65);

    do {
        printf("\n===== SISTEM DATA MAHASISWA =====\n");
        printf("1. Tampilkan semua data\n");
        printf("2. Tambah mahasiswa\n");
        printf("3. Cari mahasiswa (NIM)\n");
        printf("4. Hapus mahasiswa (NIM)\n");
        printf("5. Simpan ke CSV\n");
        printf("6. Urutkan berdasarkan nilai (Bubble Sort)\n");
        printf("0. Keluar\n");
        printf("Pilihan: ");
        scanf("%d", &pilihan);
        getchar();

        switch (pilihan) {
            case 1:
                print_table(head);
                break;

            case 2:
                printf("Nama   : "); fgets(nama, 50, stdin); nama[strcspn(nama, "\n")] = 0;
                printf("NIM    : "); fgets(nim, 15, stdin);  nim[strcspn(nim, "\n")]  = 0;
                printf("Tugas  : "); scanf("%f", &tugas);
                printf("UTS    : "); scanf("%f", &uts);
                printf("UAS    : "); scanf("%f", &uas);
                getchar();
                head = add(head, nama, nim, tugas, uts, uas);
                printf("Mahasiswa berhasil ditambahkan.\n");
                break;

            case 3:
                printf("Masukkan NIM: "); fgets(nim, 15, stdin); nim[strcspn(nim, "\n")] = 0;
                Mahasiswa *hasil = search(head, nim);
                if (hasil)
                    printf("Ditemukan: %s | NilaiAkhir: %.2f | Mutu: %s\n",
                           hasil->nama, hasil->nilai_akhir, hasil->mutu);
                else
                    printf("Mahasiswa dengan NIM %s tidak ditemukan.\n", nim);
                break;

            case 4:
                printf("Masukkan NIM yang akan dihapus: "); fgets(nim, 15, stdin); nim[strcspn(nim, "\n")] = 0;
                head = delete_nim(head, nim);
                break;

            case 5:
                save_csv(head, "data_mahasiswa.csv");
                break;

            case 6:
                head = bubble_sort(head);
                printf("Data berhasil diurutkan (tertinggi ke terendah).\n");
                print_table(head);
                break;

            case 0:
                printf("Program selesai. Sampai jumpa!\n");
                break;

            default:
                printf("Pilihan tidak valid.\n");
        }
    } while (pilihan != 0);

    free_all(head);
    return 0;
}
