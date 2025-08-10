# salea-logic-2-parser-to-bin
* Python GUI tool for converting Saleae Logic2 parsed .csv files to ImHex-compatible .bin. 
* Convert Logic2 parsed CSV files into binary files ready for reverse engineering with ImHex. 
* A small GUI-based converter for turning Logic2 CSV data into binary format.
flowchart LR
    A[Saleae Logic 2] -->|Export| B[.csv]
    B -->|logic2_parser| C[parsed.csv]
    C -->|logic2_parser_to_bin| D[.bin]
    D -->|Open in| E[ImHex Editor]

<img width="649" height="282" alt="image" src="https://github.com/user-attachments/assets/9267673d-226a-4b08-9cfc-d8d4b073cf55" />
<img width="408" height="175" alt="image" src="https://github.com/user-attachments/assets/5a80d9d1-9508-4288-be5d-3415c74bdc92" />
<img width="1916" height="1030" alt="image" src="https://github.com/user-attachments/assets/3f3e581d-c633-4625-9be5-78a40e297e5d" />
<img width="1917" height="1031" alt="image" src="https://github.com/user-attachments/assets/187c446f-d451-49bc-941b-bce3c2b1be81" />
