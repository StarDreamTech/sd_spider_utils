def json2excel(filepath):
    """
    input: filepath: string
    [
    {"name":"小明","age",18},
    ...
    ]
    """
    import os
    import json
    import pandas as pd

    # 获取输入文件所在的文件夹路径
    folder_path = os.path.dirname(filepath)
    # 获取输入文件的文件名（不带扩展名）
    file_name = os.path.splitext(os.path.basename(filepath))[0]
    # 构建输出的 Excel 文件路径
    output_filepath = os.path.join(folder_path, f"{file_name}.xlsx")
    # 读取 JSON 文件
    with open(filepath, "r", encoding="utf-8") as file:
        obj_list = json.load(file)
    # 将数据转换为 DataFrame
    df = pd.DataFrame(obj_list)
    # 将 DataFrame 保存为 Excel 文件
    df.to_excel(output_filepath, index=False)
    print(f"Excel 文件已保存：{output_filepath}")


if __name__ == "__main__":
    json2excel(r"demo.json")
