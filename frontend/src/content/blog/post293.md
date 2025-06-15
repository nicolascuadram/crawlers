---
title: "Electronics, Vol. 14, Pages 2366: Runtime Monitoring Approach to Safeguard Behavior of Autonomous Vehicles at Traffic Lights"
description: "Electronics"
url: "https://www.mdpi.com/2079-9292/14/12/2366"
type: "paper"
pubDate: "2025-06-09"
created_at: "2025-06-09 16:55:18.713574"
log_id: 59
sourcename: MDPI
author: "\"Adina Aniculaesei\",\"Yousri Elhajji\""
heroImage: /mdpi.jpg
linkDownload: "https://www.mdpi.com/2079-9292/14/12/2366"
---

Accurate traffic light status detection and the appropriate response to changes in that status are crucial for autonomous driving systems (ADSs) starting from SAE Level 3 automation. The dilemma zone problem occurs during the amber phase of traffic lights, when the ADS must decide whether to stop or proceed through the intersection. This paper proposes a methodology for developing a runtime monitor that addresses the dilemma zone problem and monitors the autonomous vehicle&amp;rsquo;s behavior at traffic lights, ensuring that the ADS&amp;rsquo;s decisions align with the system&amp;rsquo;s safety requirements. This methodology yields a set of safety requirements formulated in controlled natural language, their formal specification in linear temporal logic (LTL), and the implementation of a corresponding runtime monitor. The monitor is integrated within a safety-oriented software architecture through a modular autonomous driving system pipeline, enabling real-time supervision of the ADS&amp;rsquo;s decision-making at intersections. The results show that the monitor maintained stable and fast reaction times between 40 ms and 65 ms across varying speeds (up to 13 m/s), remaining well below the 100 ms threshold required for safe autonomous operation. At speeds of 30, 50, and 70 km/h, the system ensured correct behavior with no violations of traffic light regulations. Furthermore, the monitor achieved 100% detection accuracy of the relevant traffic lights within 76 m, with high spatial precision (&amp;plusmn;0.4 m deviation). While the system performed reliably under typical conditions, it showed limitations in disambiguating adjacent, irrelevant signals at distances below 25 m, indicating opportunities for improvement in dense urban environments.
