---
title: "Brain Sciences, Vol. 15, Pages 618: Prediction of Alzheimer&rsquo;s Disease Based on Multi-Modal Domain Adaptation"
description: ""
url: "https://www.mdpi.com/2076-3425/15/6/618"
type: "paper"
pubDate: "2025-06-07"
created_at: "2025-06-07 11:31:14.072486"
log_id: 3
sourcename: MDPI
author: "\"Binbin Fu\",\"Changsong Shen\",\"Shuzu Liao\",\"Fangxiang Wu\",\"Bo Liao\""
heroImage: /mdpi.jpg
linkDownload: "https://www.mdpi.com/2076-3425/15/6/618"
---

Background/Objectives: Structural magnetic resonance imaging (MRI) and 18-fluoro-deoxy-glucose positron emission tomography (PET) reveal the structural and functional information of the brain from different dimensions, demonstrating considerable clinical and practical value in the computer-aided diagnosis of Alzheimer&amp;rsquo;s disease (AD). However, the structure and semantics of different modal data are different, and the distribution between different datasets is prone to the problem of domain shift. Most of the existing methods start from the single-modal data and assume that different datasets meet the same distribution, but they fail to fully consider the complementary information between the multi-modal data and fail to effectively solve the problem of domain distribution difference. Methods: In this study, we propose a multi-modal deep domain adaptation (MM-DDA) model that integrates MRI and PET modal data, which aims to maximize the utilization of the complementarity of the multi-modal data and narrow the differences in domain distribution to boost the accuracy of AD classification. Specifically, MM-DDA comprises three primary modules: (1) the feature encoding module, which employs convolutional neural networks (CNNs) to capture detailed and abstract feature representations from MRI and PET images; (2) the multi-head attention feature fusion module, which is used to fuse MRI and PET features, that is, to capture rich semantic information between modes from multiple angles by dynamically adjusting weights, so as to achieve more flexible and efficient feature fusion; and (3) the domain transfer module, which reduces the distributional discrepancies between the source and target domains by employing adversarial learning training. Results: We selected 639 subjects from the Alzheimer&amp;rsquo;s Disease Neuroimaging Initiative (ADNI) and considered two transfer learning settings. In ADNI1&amp;rarr;ADNI2, the accuracies of the four experimental groups, AD vs. CN, pMCI vs. sMCI, AD vs. MCI, and MCI vs. CN, reached 92.40%, 81.81%, 81.13%, and 85.45%, respectively. In ADNI2&amp;rarr;ADNI1, the accuracies of the four experimental groups, AD vs. CN, pMCI vs. sMCI, AD vs. MCI, and MCI vs. CN, reached 94.73%, 81.48%, 85.48%, and 81.69%, respectively. Conclusions: MM-DDA is compared with other deep learning methods on two kinds of transfer learning, and the performance comparison results confirmed the superiority of the proposed method in AD prediction tasks.
