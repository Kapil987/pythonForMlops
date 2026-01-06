industry-standard ideas you can implement by tweaking your existing code:

---

## 1. Automated Customer Support Ticket Summarizer

**Industry Use:** Companies receive thousands of support emails. Instead of reading them all, they use AI to create a 2-sentence summary and determine the "sentiment" (angry or happy).

* **The Tweak:** Change the prompt to: *"Summarize the following customer ticket and rate the priority as High, Medium, or Low based on the tone."*
* **Code Change:** Update the `s3_key` to include the priority (e.g., `high_priority/ticket_01.txt`) so the support team knows what to open first.

---

## 2. Product Description Generator for E-commerce

**Industry Use:** Marketing teams often have a list of technical specs (weight, material, color) and need a catchy sales description for a website.

* **The Tweak:** Change the input `event` to take a list of features instead of a topic.
* **The Prompt:** *"You are a marketing expert. Write a persuasive product description for a website using these features: {features}."*
* **The S3 Benefit:** You can save the output as a `.html` snippet that can be directly uploaded to a web store.

---

## 3. PII (Personally Identifiable Information) Masker

**Industry Use:** Data privacy (GDPR/CCPA) is huge. Companies need to remove names and phone numbers from logs before sharing them with researchers.

* **The Tweak:** Change the prompt to: *"Redact all names, email addresses, and phone numbers from the following text and replace them with [REDACTED]."*
* **The Flow:** Your Lambda reads a "dirty" file and saves a "clean" version to the S3 bucket.

---

## 4. Multi-Language Translator for Social Media

**Industry Use:** Global brands post the same content in multiple languages.

* **The Tweak:** Modify your `body` to include a target language.
* **Code Change:**
```python
target_lang = event['language'] # e.g., "Spanish"
prompt = f"Translate the following text into {target_lang}: {text}"

```


* **The S3 Benefit:** Store files in folders organized by language: `/spanish/post1.txt`, `/french/post1.txt`.

---

## Summary of Key Changes

To implement any of these, you only need to change three small things in your current script:

| Component | What to Change |
| --- | --- |
| **Input (`event`)** | Accept more parameters (like `priority`, `language`, or `product_specs`). |
| **Prompt Logic** | Change the instructions to the Llama model from "Write a blog" to "Summarize," "Translate," or "Redact." |
| **S3 Key Logic** | Organize your output into folders (Prefixes) based on the result (e.g., `/positive/`, `/negative/`). |

