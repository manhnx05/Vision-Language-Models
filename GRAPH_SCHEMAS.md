# VLM Graph Schemas Reference

Tài liệu này định nghĩa cấu trúc JSON cho từng loại biểu đồ, dùng để train/prompt VLM.

| Graph Type | Description | Required Fields |
| :--- | :--- | :--- |
| **line** | Biểu đồ line | `title, x_label, y_label, data` |
| **bar** | Biểu đồ bar | `title, x_label, y_label, data` |
| **scatter** | Biểu đồ scatter | `title, x_label, y_label, data` |
| **pie** | Biểu đồ pie | `title, data` |
| **histogram** | Biểu đồ histogram | `title, x_label, y_label, data` |
| **boxplot** | Biểu đồ boxplot | `title, x_label, y_label, data` |
| **area** | Biểu đồ area | `title, x_label, y_label, data` |
| **bubble** | Biểu đồ bubble | `title, x_label, y_label, data` |
| **barh** | Biểu đồ barh | `title, x_label, y_label, data` |
| **donut** | Biểu đồ donut | `title, data` |
| **heatmap** | Biểu đồ heatmap | `title, x_label, y_label, data` |
| **radar** | Biểu đồ radar | `title, data` |
| **violin** | Biểu đồ violin | `title, x_label, y_label, data` |
| **stem** | Biểu đồ stem | `title, x_label, y_label, data` |
| **step** | Biểu đồ step | `title, x_label, y_label, data` |

---

## Detailed JSON Templates

### Line

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "x": "list",
  "y": "list",
  "label": "str (optional)"
}
```

**Example JSON:**
```json
{
  "graph_type": "line",
  "title": "Monthly Sales",
  "x_label": "Month",
  "y_label": "Revenue",
  "data": [
    {
      "x": [
        "Jan",
        "Feb",
        "Mar"
      ],
      "y": [
        100,
        150,
        120
      ],
      "label": "2023"
    }
  ]
}
```

---

### Bar

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "x": "list",
  "y": "list",
  "label": "str (optional)"
}
```

**Example JSON:**
```json
{
  "graph_type": "bar",
  "title": "Fruit Count",
  "x_label": "Fruit",
  "y_label": "Count",
  "data": [
    {
      "x": [
        "Apple",
        "Banana",
        "Orange"
      ],
      "y": [
        10,
        20,
        15
      ]
    }
  ]
}
```

---

### Scatter

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "x": "list",
  "y": "list",
  "label": "str (optional)"
}
```

**Example JSON:**
```json
{
  "graph_type": "scatter",
  "title": "Height vs Weight",
  "x_label": "Height",
  "y_label": "Weight",
  "data": [
    {
      "x": [
        160,
        170,
        180
      ],
      "y": [
        60,
        70,
        80
      ]
    }
  ]
}
```

---

### Pie

**Required Fields:**
- `title`
- `data`

**Data Structure:**
```json
{
  "labels": "list",
  "values": "list"
}
```

**Example JSON:**
```json
{
  "graph_type": "pie",
  "title": "Browser Usage",
  "data": [
    {
      "labels": [
        "Chrome",
        "Firefox",
        "Edge"
      ],
      "values": [
        60,
        25,
        15
      ]
    }
  ]
}
```

---

### Histogram

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "values": "list",
  "bins": "int (optional)"
}
```

**Example JSON:**
```json
{
  "graph_type": "histogram",
  "title": "Age Distribution",
  "x_label": "Age",
  "y_label": "Frequency",
  "data": [
    {
      "values": [
        22,
        25,
        25,
        30,
        35,
        40,
        45,
        50,
        55,
        60
      ]
    }
  ]
}
```

---

### Boxplot

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "values": "list",
  "label": "str"
}
```

**Example JSON:**
```json
{
  "graph_type": "boxplot",
  "title": "Exam Scores",
  "x_label": "Class",
  "y_label": "Score",
  "data": [
    {
      "label": "Class A",
      "values": [
        80,
        85,
        90,
        70,
        95
      ]
    },
    {
      "label": "Class B",
      "values": [
        75,
        80,
        85,
        60,
        90
      ]
    }
  ]
}
```

---

### Area

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "x": "list",
  "y": "list",
  "label": "str (optional)"
}
```

**Example JSON:**
```json
{
  "graph_type": "area",
  "title": "Server Load",
  "x_label": "Time",
  "y_label": "Load",
  "data": [
    {
      "x": [
        1,
        2,
        3,
        4
      ],
      "y": [
        20,
        40,
        30,
        50
      ],
      "label": "CPU"
    }
  ]
}
```

---

### Bubble

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "x": "list",
  "y": "list",
  "s": "list (sizes)",
  "label": "str (optional)"
}
```

**Example JSON:**
```json
{
  "graph_type": "bubble",
  "title": "Market Share",
  "x_label": "GDP",
  "y_label": "Growth",
  "data": [
    {
      "x": [
        10,
        20,
        30
      ],
      "y": [
        5,
        10,
        15
      ],
      "s": [
        100,
        200,
        300
      ],
      "label": "Countries"
    }
  ]
}
```

---

### Barh

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "y": "list (categories)",
  "x": "list (values)",
  "label": "str (optional)"
}
```

**Example JSON:**
```json
{
  "graph_type": "barh",
  "title": "Top Movies",
  "x_label": "Revenue",
  "y_label": "Movie",
  "data": [
    {
      "y": [
        "Movie A",
        "Movie B"
      ],
      "x": [
        100,
        200
      ]
    }
  ]
}
```

---

### Donut

**Required Fields:**
- `title`
- `data`

**Data Structure:**
```json
{
  "labels": "list",
  "values": "list"
}
```

**Example JSON:**
```json
{
  "graph_type": "donut",
  "title": "Storage Usage",
  "data": [
    {
      "labels": [
        "Used",
        "Free"
      ],
      "values": [
        70,
        30
      ]
    }
  ]
}
```

---

### Heatmap

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "matrix": "list of lists",
  "x_ticks": "list",
  "y_ticks": "list"
}
```

**Example JSON:**
```json
{
  "graph_type": "heatmap",
  "title": "Correlation Matrix",
  "x_label": "Var",
  "y_label": "Var",
  "data": [
    {
      "matrix": [
        [
          1,
          0.5
        ],
        [
          0.5,
          1
        ]
      ],
      "x_ticks": [
        "A",
        "B"
      ],
      "y_ticks": [
        "A",
        "B"
      ]
    }
  ]
}
```

---

### Radar

**Required Fields:**
- `title`
- `data`

**Data Structure:**
```json
{
  "categories": "list",
  "values": "list",
  "label": "str"
}
```

**Example JSON:**
```json
{
  "graph_type": "radar",
  "title": "Skill Set",
  "data": [
    {
      "categories": [
        "Speed",
        "Power",
        "Stamina"
      ],
      "values": [
        80,
        90,
        70
      ],
      "label": "Player 1"
    }
  ]
}
```

---

### Violin

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "values": "list",
  "label": "str"
}
```

**Example JSON:**
```json
{
  "graph_type": "violin",
  "title": "Salary Distribution",
  "x_label": "Department",
  "y_label": "Salary",
  "data": [
    {
      "label": "HR",
      "values": [
        50,
        55,
        60,
        45,
        70
      ]
    },
    {
      "label": "IT",
      "values": [
        60,
        70,
        80,
        90,
        100
      ]
    }
  ]
}
```

---

### Stem

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "x": "list",
  "y": "list",
  "label": "str (optional)"
}
```

**Example JSON:**
```json
{
  "graph_type": "stem",
  "title": "Signal Processing",
  "x_label": "Time",
  "y_label": "Amplitude",
  "data": [
    {
      "x": [
        0,
        1,
        2,
        3
      ],
      "y": [
        1,
        2,
        -1,
        0
      ]
    }
  ]
}
```

---

### Step

**Required Fields:**
- `title`
- `x_label`
- `y_label`
- `data`

**Data Structure:**
```json
{
  "x": "list",
  "y": "list",
  "label": "str (optional)"
}
```

**Example JSON:**
```json
{
  "graph_type": "step",
  "title": "Inventory Level",
  "x_label": "Time",
  "y_label": "Quantity",
  "data": [
    {
      "x": [
        1,
        2,
        3,
        4
      ],
      "y": [
        10,
        8,
        12,
        5
      ]
    }
  ]
}
```

---

