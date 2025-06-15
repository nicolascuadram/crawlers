---
title: "InformatIQ: a transformers-powered framework for practical module handbook metadata extraction"
description: "International Journal of Computers and Applications"
url: "https://www.tandfonline.com/doi/full/10.1080/1206212X.2025.2516551"
type: "paper"
pubDate: "Article |Published online: 07 Jun 2025| Views: 23"
created_at: "2025-06-09 16:56:04.474048"
log_id: 60
sourcename: Taylor & Francis
author: "Binh Vu,Sina Mehraeen,Sumeet Hande,Swati Chandna&Mehrdad Jalali"
heroImage: /blog-placeholder-3.jpg
linkDownload: "https://www.tandfonline.com/doi/full/10.1080/1206212X.2025.2516551"
---

Academic module handbooks are crucial resources containing vital course information, but their inherent non-uniformity in structure, format, and language across universities makes automated metadata extraction challenging. This paper presents a robust approach leveraging Natural Language Processing (NLP) techniques, specifically transformer-based models, to automatically extract key metadata like course titles, ECTS credits, instructors, and descriptions from diverse PDF module handbooks. We detail a pipeline involving PDF text extraction, semi-automated dataset creation using BIO tagging, and model fine-tuning. A significant challenge identified was dataset class imbalance, which severely impacted initial model performance. This was effectively addressed by implementing a weighted Cross-Entropy Loss function during the fine-tuning of BERT and DistilBERT models. Evaluated on a dataset covering five universities and both English and German languages, the fine-tuned BERT model with weighted loss achieved an accuracy and F1-score of approximately 99.8%, while the DistilBERT model also demonstrated strong performance, achieving approximately 97.8% accuracy and F1-score. These results demonstrate the efficacy of the proposed method. The study provides a practical framework, including a user interface, for efficiently converting unstructured handbook information into structured, usable data.
