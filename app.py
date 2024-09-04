import gradio as gr

from deepdoc.parser.pdf_parser import RAGFlowPdfParser

# Initialize the PDF parser
pdf_parser = RAGFlowPdfParser()


def parse_pdf(file):
    # Call the parser to get the text and tables
    text, tables = pdf_parser(file.name, need_image=False, zoomin=3, return_html=False)
    print(f"{text=}")
    print(f"{tables=}")
    return text + "\n" + "\n".join(str(obj) for obj in tables)

    # # Format the text results as specified
    # formatted_results = []
    # for item in text:
    #     formatted_item = {
    #         'id': str(uuid.uuid4()),
    #         'page': item['page_number'],
    #         'seq_no': item['seq_no'],
    #         'sentence': item['text'],
    #         'type': 'sentence',
    #         'text_location': {
    #             'location': (
    #                 (item['x0'], item['top']),
    #                 (item['x0'], item['bottom']),
    #                 (item['x1'], item['bottom']),
    #                 (item['x1'], item['top'])
    #             )
    #         }
    #     }
    #     formatted_results.append(formatted_item)
    #
    # return "\n".join(str(obj) for obj in formatted_results)


# 创建Gradio界面
iface = gr.Interface(
    fn=parse_pdf,
    inputs=gr.File(label="input", file_types=["pdf"]),
    # outputs="html",
    outputs=gr.Textbox(label="output", lines=25, show_copy_button=True),
    title="PDF Parser",
    description="Upload a PDF file to parse its content, including images, tables, and text.",
    flagging_options=None,
)

# 启动Gradio应用
iface.launch()
