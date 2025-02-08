import re
newcommand = r"""
  $$\newcommand{\R}{\mathrm{cos}(R)} 
  \newcommand{\heatflux}{q}
  \newcommand{\heatrate}{\dot{\heatflux}}
  \newcommand{\deflection}{\delta{}}
  \newcommand{\traction}{P}
  \newcommand{\youngs}{E}
  \newcommand{\secondmomentum}{I}
  \newcommand{\ndM}{\secondmomentum}
  \newcommand{\pdev}[2]{\frac{\partial{}#1}{\partial{}#2}}
  $$
  

  """
def replace_math_newcommand(input_string):
  # 搜尋字串中 #include<xxx> 的部分，並根據 xxx 的值進行替換。
  # Args:
  #   input_string: 輸入的字串。
  # Returns:
  #   替換後的字串。
  pattern = r"#include<(.*?)>"
  matches = re.findall(pattern, input_string)
  
  if not matches:
    return input_string  # 沒有找到則返回原字串

  for match in matches:
    if match == "newcommand_math":
      tab = f"<p style=\"display: none;\"><span class=\"{match}\">{newcommand}</span></p>"
      input_string = input_string.replace(f'#include<{match}>', tab)
    elif match == "bbb":
      input_string = input_string.replace(f'<span class="{match}"></span>', "")

  return input_string

def replace_terminology_translation(input_string):
  pattern = r"【(.*?)\((.*?)\)】"
  matches = re.findall(pattern, input_string)
  if not matches:
    return input_string  # 沒有找到則返回原字串

  for match in matches:
    term = match[0]
    term_en = match[1]
    tab = f"<span class=\"term\">{term}</span><span class=\"translation\">（{term_en}）</span>"
    input_string = input_string.replace(f'【{term}({term_en})】', tab)
  return input_string


def on_page_markdown(markdown, page, config, **kwargs):
  replace_fun = [replace_terminology_translation, replace_math_newcommand]
  for func in replace_fun:
    markdown = func(markdown)
    
  script = """
  文字文字
  """
  return markdown + script