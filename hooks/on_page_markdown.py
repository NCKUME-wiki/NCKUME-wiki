import re
text1 = "這是 aaa 的替換文字"
text2 = "這是 bbb 的替換文字"
newcommand = r"""$$\newcommand{\R}{\mathrm{cos}(R)} 
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
def replace_span(input_string):
  """
  搜尋字串中 <span class="xxx"></span> 的部分，並根據 xxx 的值進行替換。

  Args:
    input_string: 輸入的字串。

  Returns:
    替換後的字串。
  """
  # pattern = r"<span class=\"newcommand_(.*?)\"></span>"  # 匹配 <span class="xxx"></span>
  # matches = re.findall(pattern, input_string)
  # if not matches:
  #   return input_string  # 沒有找到則返回原字串

  # for match in matches:
  #   if match == "math":
  #     input_string = input_string.replace(f'<span class="newcommand_{match}"></span>', newcommand)
  #   elif match == "bbb":
  #     input_string = input_string.replace(f'<span class="{match}"></span>', text2)
  
  
  
  pattern = r"#include<(.*?)>"
  matches = re.findall(pattern, input_string)
  
  if not matches:
    return input_string  # 沒有找到則返回原字串

  for match in matches:
    if match == "newcommand_math":
      tag = f"<p style=\"display: none;\"><span class=\"{match}\">{newcommand}</span></p>"
      input_string = input_string.replace(f'#include<{match}>', tag)
    elif match == "bbb":
      input_string = input_string.replace(f'<span class="{match}"></span>', text2)

  return input_string



def on_page_markdown(markdown, page, config, **kwargs):
  after_re = replace_span(markdown)
  script = """
  文字文字
  """
  return after_re + script