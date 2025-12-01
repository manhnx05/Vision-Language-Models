## CẤU TRÚC PROJECT

```
vlm_graph_project/
│
├── main.py                 # File chính để chạy demo
├── requirements.txt        # Danh sách thư viện cần cài
│
├── modules/                # Thư mục chứa code chính
│   ├── graph_schemas.py    # Định nghĩa schema cho 15 loại biểu đồ
│   ├── json_validator.py   # Kiểm tra tính hợp lệ của JSON
│   ├── graph_drawer.py     # Vẽ biểu đồ bằng Matplotlib
│   ├── doc_exporter.py     # Xuất file Word
│   └── main_pipeline.py    # Kết nối các module lại với nhau
│
├── tools/                  # Công cụ hỗ trợ
│   ├── generate_examples.py    # Tạo file JSON mẫu
│   ├── generate_gallery.py     # Tạo trang web xem biểu đồ
│   └── generate_schema_docs.py # Tạo tài liệu schema
│
├── examples/               # Thư mục chứa 15 file JSON mẫu
├── outputs/                # Thư mục lưu kết quả (ảnh PNG và file Word)
└── tests/                  # Thư mục chứa unit tests
```


## CÀI ĐẶT

### Bước 1: Tải project về máy

```bash
git clone https://github.com/manhnx05/Vision-Language-Models.git
cd vlm_graph_project
```

### Bước 2: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### Các thư viện sử dụng

- matplotlib: Dùng để vẽ biểu đồ
- python-docx: Dùng để tạo file Word
- numpy: Dùng để xử lý dữ liệu số và ma trận

## HƯỚNG DẪN SỬ DỤNG

### Chạy demo với 15 file mẫu có sẵn

```bash
python main.py
```

Chương trình sẽ xử lý 15 file JSON trong thư mục examples/ và tạo ra:
- 15 file ảnh PNG trong outputs/images/
- 15 file Word trong outputs/docs/

## CÁC LOẠI BIỂU ĐỒ HỖ TRỢ

Hệ thống hỗ trợ 15 loại biểu đồ:

| STT | Tên tiếng Việt | Tên tiếng Anh | File mẫu | Công dụng |
|-----|----------------|---------------|----------|-----------|
| 1 | Biểu đồ đường | Line Chart | examples/line.json | Thể hiện xu hướng theo thời gian |
| 2 | Biểu đồ cột | Bar Chart | examples/bar.json | So sánh giá trị giữa các nhóm |
| 3 | Biểu đồ phân tán | Scatter Plot | examples/scatter.json | Xem mối tương quan giữa 2 biến |
| 4 | Biểu đồ tròn | Pie Chart | examples/pie.json | Thể hiện tỷ lệ phần trăm |
| 5 | Biểu đồ tần suất | Histogram | examples/histogram.json | Phân bố dữ liệu |
| 6 | Biểu đồ hộp | Boxplot | examples/boxplot.json | Thống kê mô tả (min, max, median) |
| 7 | Biểu đồ vùng | Area Chart | examples/area.json | Xu hướng tích lũy |
| 8 | Biểu đồ bong bóng | Bubble Chart | examples/bubble.json | So sánh 3 biến cùng lúc |
| 9 | Biểu đồ thanh ngang | Barh Chart | examples/barh.json | Xếp hạng, ranking |
| 10 | Biểu đồ vành khuyên | Donut Chart | examples/donut.json | Tỷ lệ phần trăm (có lỗ giữa) |
| 11 | Biểu đồ nhiệt | Heatmap | examples/heatmap.json | Ma trận tương quan |
| 12 | Biểu đồ mạng nhện | Radar Chart | examples/radar.json | So sánh nhiều chỉ số |
| 13 | Biểu đồ violin | Violin Plot | examples/violin.json | Phân bố mật độ dữ liệu |
| 14 | Biểu đồ thân lá | Stem Plot | examples/stem.json | Tín hiệu rời rạc |
| 15 | Biểu đồ bậc thang | Step Plot | examples/step.json | Thay đổi đột ngột |



