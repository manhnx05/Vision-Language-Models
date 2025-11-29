# VLM Graph Project - Research Pipeline

Project này là một phần của nghiên cứu về ứng dụng **Vision Language Models (VLM)** trong việc trích xuất và tái tạo thông tin từ biểu đồ.

Mục tiêu của project là xây dựng một pipeline tự động hóa:
1.  **VLM Output**: Nhận dữ liệu JSON được sinh ra từ VLM (khi VLM nhìn vào ảnh biểu đồ).
2.  **Validation**: Kiểm tra và chuẩn hóa dữ liệu JSON theo schema định nghĩa trước.
3.  **Visualization**: Vẽ lại biểu đồ chính xác từ dữ liệu JSON bằng Python (Matplotlib).
4.  **Reporting**: Xuất kết quả biểu đồ vào file văn bản (Word/Docx) để làm báo cáo.

## 📂 Cấu trúc Project

```
vlm_graph_project/
│
├── main.py                 # Script chính để chạy demo toàn bộ pipeline
├── requirements.txt        # Các thư viện Python cần thiết
│
├── modules/                # Core Logic
│   ├── graph_schemas.py    # ĐỊNH NGHĨA (DEFINE): Chứa Schema chuẩn cho 15+ loại biểu đồ
│   ├── json_validator.py   # KIỂM TRA (VALIDATE): Đảm bảo JSON từ VLM đúng cú pháp & dữ liệu
│   ├── graph_drawer.py     # VẼ (DRAW): Engine vẽ biểu đồ dùng Matplotlib
│   ├── doc_exporter.py     # XUẤT (EXPORT): Module tạo file Word (.docx)
│   └── main_pipeline.py    # Orchestrator kết nối các bước trên
│
├── tools/                  # Công cụ hỗ trợ nghiên cứu
│   ├── generate_examples.py    # Sinh lại dữ liệu mẫu từ Schema
│   ├── generate_gallery.py     # Tạo file HTML xem trước tất cả biểu đồ
│   └── generate_schema_docs.py # Sinh tài liệu Schema (Markdown) để làm Prompt cho VLM
│
├── examples/               # Dữ liệu JSON mẫu (Input giả lập từ VLM)
├── outputs/                # Kết quả đầu ra (Ảnh PNG và File DOCX)
└── tests/                  # Unit Tests đảm bảo code chạy đúng
```

## 🚀 Cài đặt

Yêu cầu: Python 3.8+

1.  Clone hoặc tải project về máy.
2.  Cài đặt các thư viện phụ thuộc:
    ```bash
    pip install -r requirements.txt
    ```

## 📖 Hướng dẫn sử dụng

### 1. Chạy Demo (Kiểm thử toàn bộ)
Để kiểm tra pipeline hoạt động với 15 loại biểu đồ mẫu:
```bash
python main.py
```
Kết quả sẽ được lưu trong thư mục `outputs/images` và `outputs/docs`.

### 2. Chạy với file JSON cụ thể
Bạn có thể import pipeline vào code của mình:
```python
from modules.main_pipeline import run_pipeline

# Chạy pipeline với 1 file JSON bất kỳ
result = run_pipeline("path/to/your_graph_data.json")

if result["status"] == "success":
    print(f"Đã tạo ảnh tại: {result['image_path']}")
    print(f"Đã tạo doc tại: {result['doc_path']}")
else:
    print(f"Lỗi: {result['error']}")
```

### 3. Sinh tài liệu Schema (Quan trọng cho VLM)
Để train hoặc prompt VLM sinh ra đúng định dạng JSON mà hệ thống chấp nhận, bạn cần cung cấp cấu trúc mẫu. Chạy lệnh sau để sinh file `GRAPH_SCHEMAS.md`:
```bash
python tools/generate_schema_docs.py
```
File này chứa bảng mapping: **Loại biểu đồ -> Các trường bắt buộc -> JSON Mẫu**.

### 4. Xem Gallery kết quả
Để xem nhanh tất cả các biểu đồ đã vẽ dưới dạng trang web:
```bash
python tools/generate_gallery.py
```
Sau đó mở file `outputs/gallery.html` bằng trình duyệt.

## 📊 Các loại biểu đồ hỗ trợ (15 loại)

Hệ thống hỗ trợ vẽ và xuất các loại biểu đồ sau:

1.  **Line Chart** (Biểu đồ đường)
2.  **Bar Chart** (Biểu đồ cột)
3.  **Scatter Plot** (Biểu đồ phân tán)
4.  **Pie Chart** (Biểu đồ tròn)
5.  **Histogram** (Biểu đồ tần suất)
6.  **Boxplot** (Biểu đồ hộp)
7.  **Area Chart** (Biểu đồ vùng)
8.  **Bubble Chart** (Biểu đồ bong bóng)
9.  **Barh Chart** (Biểu đồ thanh ngang)
10. **Donut Chart** (Biểu đồ vành khuyên)
11. **Heatmap** (Biểu đồ nhiệt)
12. **Radar Chart** (Biểu đồ mạng nhện)
13. **Violin Plot** (Biểu đồ violin)
14. **Stem Plot** (Biểu đồ thân lá)
15. **Step Plot** (Biểu đồ bậc thang)

## 🧪 Testing

Để chạy bộ kiểm thử tự động (Unit Tests):
```bash
python -m unittest tests/test_project.py
```

---
**Lưu ý cho nghiên cứu:**
- File `modules/graph_schemas.py` là nơi quan trọng nhất để đồng bộ giữa VLM và Code vẽ. Nếu VLM sinh ra trường mới, hãy cập nhật file này trước.
- Module `json_validator.py` đóng vai trò "người gác cổng", loại bỏ các kết quả ảo giác (hallucination) của VLM trước khi đưa vào vẽ.
