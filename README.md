N adalah jumlah orang yang akan dilawan Juned

M adalah kekuatan awal juned

Ai adalah kekuatan dari masing masing lawan dari Juned

Bi adalah tambahan kekuatan yang akan diterima Juned ketika menang melawan lawan 


Term:

Juned akan melawan musuh dari yang terlemah ke yang terkuat didalam Ai.

Juned hanya bisa menang bila melawan musuh yang lebih lemah atau sama kuat

Output:

Kekuatan terakhir atau terbesar Juned sebelum kalah / setelah musuh habis


Langkahnya adalah
1. Sediakan Input N dan M
2. Sediakan input Ai
3. Sediakan input Bi
4. Pisahkan N dan M
5. Transformasikan Ai menjadi array
6. Transformasikan Bi menjadi array
7. Urutkan Ai dari yang terkecil ke yang terbesar.
8. Nilai Ai harus selaras dengan nilai Bi, sesuai urutan indexnya. Bi tidak diurutkan seperti Ai
9. satu persatu menggunakan Loop, value M harus melawan value Ai[x], dari yang terkecil (sesuai urutan)
10. Value M bertambah sejumlah Bi[x] jika menang, dan melawan Ai[x+1] dan seterusnya.
11. Jika kalah atau sudah tidak ada yang bisa dilawan, maka value M tidak lagi bertambah.
12. Value M terakhir dikeluarkan sebagai output
