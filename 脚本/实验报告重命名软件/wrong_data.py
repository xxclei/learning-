import os
import random
from fpdf import FPDF
from docx import Document
# 预定义的索引表
index_table = {
    "梁展": "202283300377",
    "刘洋": "202083290157",
    "严学森": "202283290009",
    "于皓玮": "202283290013",
    "刘书涵": "202283290033",
    "吕慎远": "202283290067",
    "周敏": "202283290086",
    "周紫妍": "202283290089",
    "唐纪烨": "202283290093",
    "孟德志": "202283290116",
    "常皓杰": "202283290128",
    "常英豪": "202283290129",
    "庞相玉": "202283290130",
    "张宇": "202283290140",
    "张宇驰": "202283290141",
    "张撼天": "202283290147",
    "张瑞晨": "202283290159",
    "张逸博": "202283290165",
    "徐文哲": "202283290182",
    "施煜": "202283290200",
    "曹秉宇": "202283290208",
    "朱欢颜": "202283290220",
    "朱泽权": "202283290223",
    "林炙": "202283290265",
    "殷正阳": "202283290274",
    "汪明浩": "202283290278",
    "王广诚": "202283290294",
    "王珅": "202283290305",
    "王译曼": "202283290311",
    "章富康": "202283290327",
    "童星凯": "202283290329",
    "管恺": "202283290330",
    "胡嘉怡": "202283290335",
    "路清媛": "202283290383",
    "邓炬辉": "202283290385",
    "陈光亚": "202283290416",
    "陈阳": "202283290429",
    "韩铭佳": "202283290436",
    "黄喆": "202283290452",
    "相文坤": "202283380024",
    "王力舜": "202283720019",
    "刘付旭": "22308217"
}

# 生成错误文件名的函数
def generate_invalid_filename(student_name, student_id):
    # 错误类型包括新加入的几种
    error_type = random.choice([
        "missing_name", "missing_id", "swapped", 
        "random_error", "extra_text", "name_with_id", "reversed_name_and_id"
    ])
    file_type = random.choice(['doc'])  # 支持 doc, pdf, txt 文件
    if error_type == "missing_name":
            # 错误：缺少姓名，只留下学号
            return f"{student_id}_error.{file_type}"

    elif error_type == "missing_id":
        # 错误：缺少学号，只留下姓名
        return f"{student_name}_error.{file_type}"

    elif error_type == "swapped":
        # 错误：姓名和学号位置交换
        return f"{student_id}{student_name}_error.{file_type}"

    elif error_type == "random_error":
        # 错误：在姓名或学号中插入随机字符
        random_char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        return f"{student_name}{random_char}_error.{file_type}"

    elif error_type == "extra_text":
        # 错误：在学号和姓名之间插入多余的文本（例如“人工智能导论期中报告”）
        extra_text = random.choice(["人工智能导论期中报告", "计科4班期中报告", "人工智能期中"])
        return f"{student_id}{student_name}{extra_text}_error.{file_type}"

    elif error_type == "name_with_id":
        # 错误：在姓名中直接添加学号（例如：202283290200施煜人工智能导论期中报告）
        return f"{student_id}{student_name}人工智能期中报告_error.{file_type}"

    elif error_type == "reversed_name_and_id":
        # 错误：学号和姓名逆序（例如：常皓杰 计科4班 期中报告2）
        return f"{student_name} {student_id}期中报告2_error.{file_type}"


# 生成错误文件的函数
def generate_error_files(directory, num_files=50):
    # 从索引表中随机选择 num_files 个学生
    students = list(index_table.items())
    random.shuffle(students)
    selected_students = students[:num_files]
    
    # 创建错误命名的文件
    for student_name, student_id in selected_students:
        invalid_filename = generate_invalid_filename(student_name, student_id)
        file_path = os.path.join(directory, invalid_filename)
        
        try:
            # 判断文件类型并生成相应的文件
            if invalid_filename.endswith('.doc'):
                # 生成 doc 文件
                doc = Document()
                doc.add_paragraph("这是一个错误命名的文件，包含学号和姓名，但命名格式错误。")
                doc.save(file_path)
            elif invalid_filename.endswith('.pdf'):
                # 生成 pdf 文件
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.cell(200, 10, txt="这是一个错误命名的文件，包含学号和姓名，但命名格式错误。", ln=True)
                pdf.output(file_path)

            print(f"已创建错误文件: {invalid_filename}")
        except Exception as e:
            print(f"创建文件 {invalid_filename} 时出错: {e}")


# 示例调用函数
def main():
    directory = r"C:\Users\af\Desktop\Git\RR\txt"  # 请替换为实际的目录路径
    generate_error_files(directory)

if __name__ == "__main__":
    main()
