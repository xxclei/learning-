
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog, messagebox
import os 
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
    "刘付旭": "22308217",
}

def format(text):
    # 正则表达式匹配学号（假设学号为12或14位数字）
    student_id,name=recognize(text)
    
    
    # 替换学号
    text = re.sub(student_id, "-number-", text)
    # 替换姓名
    text = re.sub(name, "-name-", text)
    
    return text



def recognize(text):
    student_id_pattern = r"\d{8,12}"
    # 正则表达式匹配2到3个汉字姓名
    name_pattern2 = r"[\u4e00-\u9fa5]{2}"
    name_pattern3 = r"[\u4e00-\u9fa5]{3}"
    name_pattern4 = r"[\u4e00-\u9fa5]{4}"

    # 提取学号和各种长度的姓名
    student_id = None
    name = None

    # 提取所有学号和姓名
    student_ids = re.findall(student_id_pattern, text)
    student_ids = re.findall(student_id_pattern, text)
    names2 = re.findall(name_pattern2, text)
    names3 = re.findall(name_pattern3, text)
    names4 = re.findall(name_pattern4, text)

    # 合并所有的姓名匹配（2个、3个、4个汉字）
    names = names2 + names3 + names4


    print(f"提取的可能的学号: {student_ids}")
    print(f"提取的可能的姓名: {names}")

    # 提取学号和姓名


    # 如果有学号，则从文本中提取学号
    if student_ids:
        for student_idd in student_ids:
            if student_idd in index_table.values():
                student_id=student_idd

    # 如果文本中有姓名，选择第一个匹配，并确保它在索引表中
    if names:
        for name1 in names:
            if name1 in index_table:
                print("识别到性名"+str(name1))
                name=name1


    # 如果文本中缺少学号，则根据姓名从索引表中查找学号
    if student_id is None and name is not None:
        student_id = index_table.get(name, None)
    
    # 如果文本中缺少姓名，则根据学号从索引表中查找姓名
    if name is None and student_id is not None:
        print("缺少姓名")
        for student_name, student_number in index_table.items():
            if student_number == student_id:
                name = student_name
                break

    return student_id,name

def generate_formatted_text(text, format_text):  #修正格式
    # 正则表达式匹配学号（8到12位数字）
    
    student_id,name=recognize(text)

    # 如果学号和姓名都存在，进行格式化
    if student_id and name:
        formatted_text_result = format_text.replace("-number-", student_id).replace("-name-", name)
        return formatted_text_result
    else:
        # 如果无法识别学号或姓名，返回错误信息
        return text + " 转化失败"

def choose_file_and_process():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 弹出文件选择对话框
    file_path = filedialog.askopenfilename(title="选择一个命名正确的文件读取实验名(不要选择学号位数非12位，可能有问题)", filetypes=[ ("All Files", "*.*")])

    if file_path:  # 如果用户选择了文件
        # 获取文件名（去掉扩展名）和目录
        file_name_without_extension, _ = os.path.splitext(os.path.basename(file_path))  # 去掉扩展名
        print(file_name_without_extension)
        file_directory = os.path.dirname(file_path)  # 获取文件的目录
        return file_name_without_extension, file_directory  # 返回去掉扩展名的文件名和目录
    else:
        return None, None
    
def confirm_and_edit_format(text):
    # 生成初步的格式化文本
    formatted_text = format(text)
    updated_text_ = formatted_text

    # 创建一个新的窗口
    edit_window = tk.Toplevel()
    edit_window.title("编辑格式")
    edit_window.geometry("600x400")

    # 创建一个Text控件，用于显示和编辑格式化后的文本
    text_box = tk.Text(edit_window, wrap=tk.WORD, height=4, font=('Arial', 18))  # 设置更大的字体
    text_box.pack(expand=True, fill=tk.BOTH)

    # 将初始的格式化文本插入到文本框中
    text_box.insert(tk.END, formatted_text)

    # 标签，用于显示动态生成的文件名
    dynamic_label = tk.Label(edit_window, text="生成的文件名：", font=('SimHei', 16))  # 设置字体大小
    dynamic_label.pack(pady=10)

    # 动态显示格式化后的文件名
    formatted_filename_label = tk.Label(edit_window, text=generate_formatted_text(text, formatted_text), font=('SimHei', 16))
    formatted_filename_label.pack(pady=20)

    # 提示标签
    format_tip_label = tk.Label(edit_window, text="-name- 为名字  -number- 为学号", font=('SimHei', 14), fg='gray')
    format_tip_label.pack(pady=10)

    # 当文本框内容发生变化时，更新动态显示的格式化结果
    def on_text_change(event):
        updated_text = text_box.get(1.0, tk.END).strip()  # 获取文本框中的最新内容
        new_formatted_filename = generate_formatted_text(text, updated_text)  # 根据新的内容生成文件名
        formatted_filename_label.config(text=new_formatted_filename)  # 更新标签显示

    # 绑定文本框内容变化事件
    text_box.bind("<KeyRelease>", on_text_change)  # 监听键盘释放事件，触发实时更新

    # 保存按钮
    def save_changes():
        updated_text = text_box.get(1.0, tk.END).strip()  # 获取修改后的文本
        return updated_text  # 返回修改后的文本

    # 确认按钮
    def confirm():
        nonlocal updated_text_  # 使用 nonlocal 来修改外部函数中的变量
        updated_text_ = save_changes()  # 获取修改后的文本
        print("updated_text=" + str(updated_text_))
        messagebox.showinfo("保存成功", "文本已重命名！")
        edit_window.quit()  # 退出事件循环
        edit_window.destroy()  # 销毁窗口

    # 取消按钮
    def cancel():
        nonlocal updated_text_ 
        updated_text_=None
        edit_window.destroy()  # 销毁窗口
        return None

    # 按钮美化：可以设置字体、大小、颜色等
    def create_large_button(window, text, command):
        return tk.Button(
            window, 
            text=text, 
            command=command,
            width=10,  # 设置按钮的宽度
            height=1,  # 设置按钮的高度
            font=('simei', 14, 'bold'),  # 设置字体及大小
            bg='black',  # 设置背景颜色
            fg='white',  # 设置字体颜色
            relief='raised',  # 按钮的边框效果
            bd=5,  # 按钮边框厚度
            activebackground='#45a049',  # 鼠标悬停时的背景颜色
            activeforeground='white'  # 鼠标悬停时的字体颜色
        )

    # 创建确认、取消按钮
    confirm_button = create_large_button(edit_window, "确认", confirm)
    confirm_button.pack(side=tk.LEFT, padx=20, pady=10)

    cancel_button = create_large_button(edit_window, "取消", cancel)
    cancel_button.pack(side=tk.RIGHT, padx=20, pady=10)

    # 启动事件循环
    edit_window.wait_window()  # 等待窗口关闭后继续执行代码

    # 获取确认后的返回值
    return updated_text_  # 返回修改后的文本

def batch_rename_files(directory, format_text):
    # 获取目录下所有文件
    files = os.listdir(directory)
    
    # 遍历每个文件
    for file_name in files:
        old_file_path = os.path.join(directory, file_name)
        
        # 跳过文件夹
        if os.path.isdir(old_file_path):
            continue
        
        # 分离文件名和后缀名
        file_name_without_extension, file_extension = os.path.splitext(file_name)
        
        # 使用文件名生成格式化的文件名（不修改扩展名部分）
        new_file_name = generate_formatted_text(file_name_without_extension, format_text) + file_extension
        new_file_path = os.path.join(directory, new_file_name)
        
        # 如果格式化名称和旧名称不同，则执行重命名
        if new_file_name != file_name:
            try:
                # 重命名文件
                os.rename(old_file_path, new_file_path)
                print(f"文件 {file_name} 已重命名为 {new_file_name}")
            except Exception as e:
                print(f"文件重命名失败: {e}")
        else:
            print(f"文件 {file_name} 无需重命名")


def show_student_list():
    # 打开学生列表窗口
    student_list_window = tk.Toplevel()
    student_list_window.title("学生列表")
    student_list_window.geometry("500x800")

    # 提示标签，指示数据格式
    format_tip_label = tk.Label(
        student_list_window,
        text="每行输入：姓名 学号 (姓名和学号之间用空格分隔)  ",
        font=('SimHei', 14),  # 黑体字体，字体大小 14
        fg='gray'
    )
    temp_warning_label = tk.Label(
        student_list_window,
        text="提示：修改仅在当前会话中有效，关闭后会丢失。",
        font=('SimHei', 12),  # 字体大小 12
        fg='red'
    )
    temp_warning_label.pack(pady=10)

    format_tip_label.pack(pady=10)

    # 创建可编辑的 Text 控件
    text_box = tk.Text(student_list_window, wrap=tk.WORD, font=('SimHei', 14))  # 黑体字体，字体大小 14
    text_box.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # 显示所有学生，格式为：姓名 学号
    for name, student_id in index_table.items():
        text_box.insert(tk.END, f"{name} {student_id}\n")

    # 保存修改后的学生列表
    def save_student_list():
        updated_lines = text_box.get(1.0, tk.END).strip().split("\n")
        new_index_table = {}
        for line in updated_lines:
            parts = line.split()
            if len(parts) == 2:  # 确保每行都有两个部分：姓名和学号
                new_index_table[parts[0]] = parts[1]
        # 更新索引表
        index_table.clear()
        index_table.update(new_index_table)
        messagebox.showinfo("保存成功", "学生列表已更新！")

    # 美化按钮：设置字体、宽度、高度、背景颜色等
    def create_large_button(window, text, command):
        return tk.Button(
            window, 
            text=text, 
            command=command,
            width=10,  # 设置按钮宽度
            height=1,  # 设置按钮高度
            font=('SimHei', 14),  # 设置黑体字体
            bg='black',  # 背景颜色为黑色
            fg='white',  # 字体颜色为白色
            relief='raised',  # 按钮边框效果
            bd=3,  # 按钮边框厚度
            activebackground='#4CAF50',  # 鼠标悬停时的背景颜色
            activeforeground='white',  # 鼠标悬停时的字体颜色
        )

    # 创建保存按钮
    save_button = create_large_button(student_list_window, "保存修改", save_student_list)
    save_button.pack(pady=20)

    # 创建关闭按钮
    close_button = create_large_button(student_list_window, "关闭", student_list_window.destroy)
    close_button.pack(pady=10)

    # 启动事件循环
    student_list_window.mainloop()


def main_window():
    root = tk.Tk()
    root.geometry("600x300")
    root.title("文件重命名工具")


    view_button = tk.Button(
        root, 
        text="查看学生列表", 
        command=show_student_list, 
        width=30, 
        height=1, 
        font=('SimHei', 14),
        relief='raised',  # 设置按钮为立体效果
        bd=5,  # 设置按钮边框厚度
        highlightthickness=2,  # 设置焦点的边框厚度
        bg='black',  # 设置背景颜色
        fg='white',  # 设置字体颜色
        activebackground='#45a049',  # 鼠标悬停时的背景颜色
        activeforeground='white',  # 鼠标悬停时的字体颜色
        padx=20,  # 按钮内左侧的边距
        pady=10,  # 按钮内顶部的边距
    )
    view_button.pack(pady=54)

    rename_button = tk.Button(
        root, 
        text="开始文件重命名", 
        command=main_function, 
        width=30, 
        height=1, 
        font=('SimHei', 14),
        relief='raised',  # 设置按钮为立体效果
        bd=5,  # 设置按钮边框厚度
        highlightthickness=2,  # 设置焦点的边框厚度
        bg='black',  # 设置背景颜色
        fg='white',  # 设置字体颜色
        activebackground='#45a049',  # 鼠标悬停时的背景颜色
        activeforeground='white',  # 鼠标悬停时的字体颜色
        padx=20,  # 按钮内左侧的边距
        pady=10,  # 按钮内顶部的边距
    )
    rename_button.pack(pady=10)
    developer_label = tk.Label(
    root, 
    text="开发者: 22计科4班zrc 有bug请及时反馈", 
    font=('SimHei', 6),  # 字体和大小
    fg='gray',  # 字体颜色为灰色
    )
    developer_label.place(x=550, y=300, anchor='se')  # 定位在右下角，`anchor='se'`表示右下角锚点

    root.mainloop()

def main_function():
    # 用户选择文件并获取文件内容及文件夹路径
    while True:
        text, directory = choose_file_and_process()

        if text:
            print("选择的文件名：" + str(text))

            # 确认和修改格式
            formatted_text = confirm_and_edit_format(text)
           
            if formatted_text is None:
                # 如果用户点击了取消，我们重新开始选择文件
                print("用户取消了操作，重新选择文件...")
                continue
            else:
                print("正确的命名方式为：" + str(formatted_text))
                # 批量重命名文件
                batch_rename_files(directory, formatted_text)

                # 生成最终格式化文本并显示
                result = generate_formatted_text(text, formatted_text)
                print("最终格式化结果：" + result)
                break
        else:
            print("没有选择文件")
            break

if __name__ == "__main__":
    main_window()