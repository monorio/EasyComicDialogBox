from PIL import Image, ImageDraw, ImageFont
import os
import shutil
import re


def add_dialogue_box(source_list, root_path, output_path, MIN_SET = -1.0, font_type_path='C:/Windows/Fonts/Dengb.ttf'):
    '''
    为图片添加对话框
    :param source_list: 一个列表，每个元素是一个列表，第一个元素是图片路径，之后都是对话内容
    :return:
    '''

    img_name = source_list[0].replace('p', '')
    image_path = f'{root_path}{img_name}.png'

    print(image_path)
    if not os.path.exists(image_path):
        print(f'{image_path} not exist')
        return

    # 打开图片和文本文件
    img = Image.open(image_path)
    original_img_width, original_img_height = img.size


    # 设置对话框的大小和颜色

    dialogue_box_height = original_img_height // 6

    new_img = Image.new('RGBA', (original_img_width, original_img_height + dialogue_box_height), (255, 255, 255, 0))
    new_img.paste(img, (0, 0))

    draw = ImageDraw.Draw(new_img)

    dialogue_box_color = (255, 255, 255)  # 白色
    img_width, img_height = new_img.size

    lines = source_list[1:]
    lines = [line for line in lines if line != '']
    longest_line = len(max(lines, key=len))

    line_para = 4
    init_font_size = int(dialogue_box_height * 1 / line_para)

    while True:

        if longest_line>=img_width//init_font_size:
            word_count = img_width//init_font_size
            mod_lines = [line[i:i+word_count] if len(line) > word_count else line for line in lines for i in range(0, len(line), word_count)]
        else:
            mod_lines = lines

        if len(mod_lines) >= line_para:
            line_para += 1
            init_font_size = int(dialogue_box_height * 1 / line_para)

            longest_line = len(max(lines, key=len))
            continue
        else:
            font_size = init_font_size + float(MIN_SET)
            break


    font_path = font_type_path

    font = ImageFont.truetype(font_path, font_size, encoding='utf-16')

    # 逐行在图片下方绘制对话框和文本
    y_offset = img_height - dialogue_box_height
    draw.rectangle([(0, y_offset), (img_width, img_height)], fill=dialogue_box_color)

    for line in mod_lines:
        line = line.strip()
        if line:
            print(line)

        draw.text((10, y_offset + 5), line, fill=(0, 0, 0), font=font)
        # 更新y偏移量
        y_offset += font_size+5

    # 保存结果图片
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    img_output = f'{output_path}{img_name}.png'
    new_img.save(img_output)


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def rename_images(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    image_files = sorted(image_files, key=natural_sort_key)
    print(image_files)

    output_folder = f'{folder_path}/sorted/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, image_file in enumerate(image_files, start=1):
        old_path = os.path.join(folder_path, image_file)
        new_path = os.path.join(output_folder, f"{i}.png")

        shutil.copy(old_path, new_path)



def generate_dialogue_parameter(script_path):
    with open(script_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    result_list = []
    current_sublist = None
    for line in lines:
        if line[0].isdigit():
            # 如果元素以数字开头，则创建一个新的内部列表
            if current_sublist is not None:
                result_list.append(current_sublist)

            current_sublist = [line.strip()]  # 创建新的内部列表并添加元素
        elif current_sublist is not None:
            # 如果不是以数字开头且当前有内部列表，则添加到当前内部列表
            current_sublist.append(line.strip())
        # 添加最后一个内部列表
    if current_sublist is not None:
        result_list.append(current_sublist)
    return result_list

def apply_folder(folder_path, MIN_SET = -1.0, font_type_path='C:/Windows/Fonts/Dengb.ttf'):
    res_list = generate_dialogue_parameter(f'{folder_path}/script.txt')
    for i in res_list:
        img_name = i[0].replace('p', '')
        image_path = f'{folder_path}/{img_name}.png'

        add_dialogue_box(i, f'{folder_path}/', f'{folder_path}/output/', MIN_SET=MIN_SET, font_type_path=font_type_path)

if __name__ == '__main__':
    apply_folder('demo', MIN_SET=0, font_type_path='C:/Windows/Fonts/Dengb.ttf')
    # rename_images('demo')
