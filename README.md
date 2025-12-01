# ĐỒ ÁN: HỆ THỐNG TÁI TẠO BIỂU ĐỒ TỪ JSON SỬ DỤNG VLM

## GIỚI THIỆU

Đồ án này nghiên cứu ứng dụng Vision Language Models (VLM) trong việc trích xuất và tái tạo thông tin từ biểu đồ. Hệ thống nhận đầu vào là dữ liệu JSON (được sinh ra từ VLM khi phân tích ảnh biểu đồ), sau đó validate, vẽ lại biểu đồ và xuất báo cáo Word.

### Mục tiêu

1. Nhận dữ liệu JSON từ VLM (khi VLM nhìn vào ảnh biểu đồ)
2. Kiểm tra và chuẩn hóa dữ liệu JSON theo schema định nghĩa trước
3. Vẽ lại biểu đồ chính xác từ dữ liệu JSON bằng Python (Matplotlib)
4. Xuất kết quả biểu đồ vào file Word để làm báo cáo

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

## YÊU CẦU HỆ THỐNG

- Python phiên bản 3.8 trở lên
- Hệ điều hành: Windows, Linux hoặc macOS
- RAM tối thiểu 2GB
- Dung lượng ổ cứng: 500MB

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

### Cách 1: Chạy demo với 15 file mẫu có sẵn

```bash
python main.py
```

Chương trình sẽ xử lý 15 file JSON trong thư mục examples/ và tạo ra:
- 15 file ảnh PNG trong outputs/images/
- 15 file Word trong outputs/docs/

### Cách 2: Test với file JSON tự tạo

Bước 1: Tạo file JSON (ví dụ: my_chart.json)

```json
{
  "graph_type": "bar",
  "title": "Điểm thi môn AI",
  "x_label": "Sinh viên",
  "y_label": "Điểm",
  "data": [
    {"x": ["An", "Bình", "Chi"], "y": [8, 9, 7]}
  ]
}
```

Bước 2: Chạy code Python

```python
from modules.main_pipeline import run_pipeline

result = run_pipeline("my_chart.json")

if result["status"] == "success":
    print("Thành công!")
    print("Ảnh:", result['image_path'])
    print("Word:", result['doc_path'])
else:
    print("Lỗi:", result['error'])
```

### Cách 3: Tạo tài liệu schema cho VLM

```bash
python tools/generate_schema_docs.py
```

Lệnh này sẽ tạo file GRAPH_SCHEMAS.md chứa cấu trúc JSON mẫu cho 15 loại biểu đồ. File này dùng để làm prompt cho VLM.

### Cách 4: Xem tất cả biểu đồ dạng web

```bash
python tools/generate_gallery.py
```

Sau đó mở file outputs/gallery.html bằng trình duyệt để xem tất cả biểu đồ đã vẽ.

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

## KIỂM THỬ

Chạy unit tests để kiểm tra hệ thống:

```bash
python -m unittest tests/test_project.py
```

Kết quả mong đợi:

```
test_pipeline_execution ... ok
test_validator_invalid_type ... ok
test_validator_missing_field ... ok
test_validator_valid ... ok

----------------------------------------------------------------------
Ran 4 tests in 2.367s

OK
```

## XỬ LÝ LỖI THƯỜNG GẶP

### Lỗi 1: Warning về legend

```
UserWarning: No artists with labels found to put in legend.
```

Nguyên nhân: Dữ liệu không có trường "label"
Giải pháp: Thêm "label": "Tên nhãn" vào data, hoặc bỏ qua (không ảnh hưởng kết quả)

### Lỗi 2: Thiếu trường bắt buộc

```
Validation failed: Missing required field: 'title'
```

Nguyên nhân: JSON thiếu trường bắt buộc
Giải pháp: Xem file GRAPH_SCHEMAS.md để biết các trường bắt buộc

### Lỗi 3: Sai tên loại biểu đồ

```
Validation failed: Unsupported graph_type: 'barchart'
```

Nguyên nhân: Tên loại biểu đồ không đúng
Giải pháp: Dùng đúng tên: bar, line, pie, scatter, histogram, boxplot, area, bubble, barh, donut, heatmap, radar, violin, stem, step

### Lỗi 4: Lỗi cú pháp JSON

```
Invalid JSON: Expecting ',' delimiter
```

Nguyên nhân: Thiếu dấu phẩy, ngoặc hoặc dấu ngoặc kép
Giải pháp: Kiểm tra lại cú pháp JSON

### Lỗi 5: Không tìm thấy file

```
File not found: path/to/file.json
```

Nguyên nhân: Đường dẫn file sai
Giải pháp: Kiểm tra lại đường dẫn, dùng đường dẫn tuyệt đối nếu cần

## MỞ RỘNG HỆ THỐNG

### Thêm loại biểu đồ mới

Bước 1: Mở file modules/graph_schemas.py và thêm schema mới

```python
GRAPH_SCHEMAS = {
    # ... các schema có sẵn ...
    "waterfall": {
        "required_fields": ["title", "x_label", "y_label", "data"],
        "data_structure": {
            "x": "list",
            "y": "list"
        },
        "sample": {
            "graph_type": "waterfall",
            "title": "Cash Flow",
            "x_label": "Category",
            "y_label": "Amount",
            "data": [{"x": ["Start", "Income", "Expense"], "y": [100, 50, -30]}]
        }
    }
}
```

Bước 2: Mở file modules/graph_drawer.py và thêm code vẽ

```python
elif graph_type == "waterfall":
    # Code vẽ waterfall chart ở đây
    pass
```

Bước 3: Tạo file JSON mẫu và test

### Tùy chỉnh giao diện biểu đồ

Mở file modules/graph_drawer.py và chỉnh sửa:

```python
# Thay đổi kích thước
plt.figure(figsize=(12, 8))  # Mặc định là (10, 6)

# Thay đổi màu sắc
plt.plot(x, y, color='red', linewidth=2)

# Thay đổi font chữ
plt.title(title, fontsize=16, fontweight='bold')
```

## KẾ HOẠCH PHÁT TRIỂN

### Giai đoạn 1: Hoàn thành (Hiện tại)

- Đã hoàn thành: Định nghĩa schema cho 15 loại biểu đồ
- Đã hoàn thành: Module validation
- Đã hoàn thành: Module vẽ biểu đồ
- Đã hoàn thành: Module xuất Word
- Đã hoàn thành: Unit tests

### Giai đoạn 2: Tích hợp VLM (Kế hoạch)

- Tích hợp model Qwen2.5-VL (3B hoặc 7B)
- Xử lý ảnh biểu đồ đầu vào
- Tạo prompt cho VLM
- Xử lý nhiều ảnh cùng lúc

### Giai đoạn 3: Đánh giá và Metrics (Kế hoạch)

- Tạo dataset chuẩn (ảnh + JSON đúng)
- Tính toán độ chính xác (Accuracy, Precision, Recall)
- So sánh ảnh gốc và ảnh vẽ lại
- Phân tích lỗi
- So sánh các VLM khác nhau

### Giai đoạn 4: Tính năng nâng cao (Tương lai)

- Hỗ trợ biểu đồ 3D
- Hỗ trợ tiếng Anh
- Tạo giao diện web
- Tạo API
- Deploy lên Colab hoặc HuggingFace

## TÀI LIỆU THAM KHẢO

- GRAPH_SCHEMAS.md: Chi tiết cấu trúc JSON cho từng loại biểu đồ
- Matplotlib: https://matplotlib.org/stable/
- Qwen2.5-VL: https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct
- Python-docx: https://python-docx.readthedocs.io/

## LƯU Ý QUAN TRỌNG

### Về code

- File modules/graph_schemas.py là file quan trọng nhất, chứa định nghĩa schema cho tất cả loại biểu đồ
- File modules/json_validator.py giúp lọc bỏ dữ liệu sai từ VLM
- Luôn validate JSON trước khi vẽ biểu đồ
- Sử dụng file GRAPH_SCHEMAS.md làm prompt cho VLM





Năm học: 2024-2025
