# modules/graph_drawer.py
import matplotlib.pyplot as plt
import numpy as np
import os

def draw_graph(json_data, output_path):
    """
    Draws a graph based on json_data and saves it to output_path.
    
    Args:
        json_data (dict): Validated JSON data.
        output_path (str): Path to save the image.
        
    Returns:
        str: The output path if successful.
    """
    graph_type = json_data.get("graph_type")
    title = json_data.get("title", "Graph")
    x_label = json_data.get("x_label", "")
    y_label = json_data.get("y_label", "")
    data = json_data.get("data", [])

    # Create a figure
    plt.figure(figsize=(10, 6))
    plt.title(title)
    
    # Common cleanup/setup
    # Note: Some plots might need specific setup, handled in blocks below.

    try:
        if graph_type == "line":
            for series in data:
                plt.plot(series["x"], series["y"], label=series.get("label"))
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()

        elif graph_type == "bar":
            # Handling multiple series for bar charts can be complex (grouped).
            # Simplified: Plotting first series or stacking/overlaying if multiple.
            # For this demo, we assume simple bars or side-by-side if possible.
            # Let's do simple overlay or just iterate.
            for i, series in enumerate(data):
                plt.bar(series["x"], series["y"], label=series.get("label"), alpha=0.7)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()

        elif graph_type == "scatter":
            for series in data:
                plt.scatter(series["x"], series["y"], label=series.get("label"))
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()

        elif graph_type == "pie":
            # Pie usually takes one dataset
            if data:
                series = data[0]
                plt.pie(series["values"], labels=series["labels"], autopct='%1.1f%%')

        elif graph_type == "histogram":
            for series in data:
                bins = series.get("bins", 10)
                plt.hist(series["values"], bins=bins, label=series.get("label"), alpha=0.7)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()

        elif graph_type == "boxplot":
            # Boxplot expects a list of arrays
            values_list = [series["values"] for series in data]
            labels_list = [series.get("label", "") for series in data]
            plt.boxplot(values_list, labels=labels_list)
            plt.xlabel(x_label)
            plt.ylabel(y_label)

        elif graph_type == "area":
            for series in data:
                plt.fill_between(series["x"], series["y"], label=series.get("label"), alpha=0.5)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()

        elif graph_type == "bubble":
            for series in data:
                # 's' is size
                sizes = series.get("s", [20] * len(series["x"]))
                plt.scatter(series["x"], series["y"], s=sizes, label=series.get("label"), alpha=0.5)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()

        elif graph_type == "barh":
            for series in data:
                plt.barh(series["y"], series["x"], label=series.get("label"), alpha=0.7)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()

        elif graph_type == "donut":
            if data:
                series = data[0]
                # Pie with a hole
                plt.pie(series["values"], labels=series["labels"], autopct='%1.1f%%', wedgeprops=dict(width=0.3))

        elif graph_type == "heatmap":
            if data:
                series = data[0]
                matrix = series["matrix"]
                x_ticks = series.get("x_ticks", [])
                y_ticks = series.get("y_ticks", [])
                cax = plt.imshow(matrix, cmap='viridis', interpolation='nearest')
                plt.colorbar(cax)
                if x_ticks:
                    plt.xticks(np.arange(len(x_ticks)), x_ticks)
                if y_ticks:
                    plt.yticks(np.arange(len(y_ticks)), y_ticks)
            plt.xlabel(x_label)
            plt.ylabel(y_label)

        elif graph_type == "radar":
            # Radar chart needs polar axes
            plt.clf() # Clear the default figure
            fig = plt.figure(figsize=(8, 8))
            ax = fig.add_subplot(111, polar=True)
            
            for series in data:
                categories = series["categories"]
                values = series["values"]
                # Close the loop
                values = values + [values[0]]
                angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
                angles += [angles[0]]
                
                ax.plot(angles, values, label=series.get("label"))
                ax.fill(angles, values, alpha=0.25)
                ax.set_xticks(angles[:-1])
                ax.set_xticklabels(categories)
            
            plt.title(title)
            plt.legend()

        elif graph_type == "violin":
            values_list = [series["values"] for series in data]
            # Violinplot doesn't support labels directly in the call easily like boxplot for x-axis
            # We need to set ticks manually
            parts = plt.violinplot(values_list, showmeans=False, showmedians=True)
            labels_list = [series.get("label", str(idx+1)) for idx, series in enumerate(data)]
            plt.xticks(np.arange(1, len(labels_list) + 1), labels_list)
            plt.xlabel(x_label)
            plt.ylabel(y_label)

        elif graph_type == "stem":
            for series in data:
                plt.stem(series["x"], series["y"], label=series.get("label"))
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()

        elif graph_type == "step":
            for series in data:
                plt.step(series["x"], series["y"], label=series.get("label"))
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.legend()

        else:
            plt.close()
            raise ValueError(f"Unsupported graph type for drawing: {graph_type}")

        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        plt.savefig(output_path)
        plt.close()
        return output_path

    except Exception as e:
        plt.close()
        raise RuntimeError(f"Failed to draw graph: {str(e)}")
