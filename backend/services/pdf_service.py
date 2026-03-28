import os
import uuid
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


# =========================
# PDF GENERATION
# =========================
def generate_gap_pdf(gaps):
    filename = f"data/pdfs/{uuid.uuid4()}.pdf"
    os.makedirs("data/pdfs", exist_ok=True)

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Research Gap Analysis", styles['Title']))
    elements.append(Spacer(1, 12))

    for paper in gaps:
        elements.append(Paragraph(paper.get("title", "No Title"), styles['Heading2']))
        elements.append(Paragraph(paper.get("gap", "No Gap Found"), styles['BodyText']))
        elements.append(Spacer(1, 12))

    doc.build(elements)
    return filename


# =========================
# TEXT EXTRACTION
# =========================
def parse_text(file_path):
    import fitz  # PyMuPDF

    try:
        doc = fitz.open(file_path)
        text = ""

        for page in doc:
            text += page.get_text()

        return text

    except Exception as e:
        return f"Error parsing text: {str(e)}"

    finally:
        try:
            doc.close()
        except:
            pass


# =========================
# IMAGE EXTRACTION
# =========================
def parse_images(file_path):
    import fitz
    import os

    image_paths = []

    try:
        doc = fitz.open(file_path)
        os.makedirs("images", exist_ok=True)

        for page_index, page in enumerate(doc):
            images = page.get_images(full=True)

            for img_index, img in enumerate(images):
                try:
                    xref = img[0]
                    base_image = doc.extract_image(xref)

                    path = f"images/page{page_index}_img{img_index}.png"

                    with open(path, "wb") as f:
                        f.write(base_image["image"])

                    image_paths.append(path)

                except Exception as img_err:
                    print(f"Image extraction error: {img_err}")

        return image_paths

    except Exception as e:
        return []

    finally:
        try:
            doc.close()
        except:
            pass


# =========================
# OCR (FOR SCANNED PDFs)
# =========================
def parse_ocr(file_path):
    import fitz
    import pytesseract
    from PIL import Image

    text = ""

    try:
        doc = fitz.open(file_path)

        for page in doc:
            try:
                pix = page.get_pixmap()

                img = Image.frombytes(
                    "RGB",
                    [pix.width, pix.height],
                    pix.samples
                )

                # Improve OCR accuracy
                img = img.convert("L")  # grayscale

                text += pytesseract.image_to_string(img)

            except Exception as page_err:
                print(f"OCR page error: {page_err}")

        return text

    except Exception as e:
        return f"OCR failed: {str(e)}"

    finally:
        try:
            doc.close()
        except:
            pass