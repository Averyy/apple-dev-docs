# Data Completeness and Corrections

**Framework**: Analytics Reports

Understand how the Analytics Reports API provides complete data sets.

#### Overview

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections. Each data batch has a start date, represented by the Date column, and a length of time, represented by `granularity` of the instance. `processingDate` is the date when Apple creates a new report instance.

These reports use this data completeness approach:

- [`AirPlay Errors`](airplay-errors.md)
- [`AirPlay Performance`](airplay-performance.md)
- [`App Clip Usage`](app-clip-usage.md)
- [`App Crashes`](app-crashes.md)
- [`App Installs Performance`](app-installs-performance.md)
- [`App Sessions`](app-sessions.md)
- [`App Store Discovery and Engagement`](app-store-discovery-and-engagement.md)
- [`App Store Downloads`](app-download.md)
- [`App Store Installations and Deletions`](app-installs.md)
- [`App Store Opt-in`](app-store-opt-in.md)
- [`App Store Pre-orders`](app-store-pre-order.md)
- [`App Store Purchases`](app-store-purchase.md)
- [`App Store Web Preview`](app-store-web-preview.md)
- [`Browser Choice Screen Engagement (iOS versions before 18.2)`](browser-choice-screen-engagement.md)
- [`Platform App Installs`](platform-app-installs.md)
- [`Streaming Downloads Performance`](streaming-downloads-performance.md)
- [`Streaming Playback Performance`](streaming-playback-performance.md)

> **Note**: For reports not listed here, see the Completeness section in each report.

For reports not listed here, see the Completeness section in each report.

For example, if you review a report instance with  `granularity` and a `processingDate` of `2024-04-01`, you might find that the Date column contains multiple dates, going back as far as the completeness threshold for that report. In this case you might find records with `2024-03-31` and `2024-03-30` in the Date column, and possibly more.

Instances from a more recent `processingDate` overwrite instances with an earlier `processingDate`. The report instance with a `processingDate` of `2024-04-01` overwrites a set of records for a `Date` of `2024-03-30` from a report instance with a `processingDate` of `2024-03-31`. Don’t merge records for a Date of `2024-03-30` across two report instances to avoid double counting. Use the latest instance.

Alternatively, you can choose to wait until data is finalized (see the Completeness description in the Overview on each report page) and download once.

> **Note**: In rare cases of data corrections, you might receive new record sets for a date in the past, beyond the completeness threshold.

In rare cases of data corrections, you might receive new record sets for a date in the past, beyond the completeness threshold.

#### Platforms

In reports with data from iPad, the Device column shows `iPad`, and the Platform version column shows `iOS` with the corresponding version number.

#### Data Completeness for Daily Weekly and Monthly Reports

In this example the report has a completeness of two days. You can wait 2 days and download final complete daily set of records for Date of 2024-03-30 from the report instance with `processingDate` of 2024-04-01 and with daily `granularity`. The Daily, Weekly, and Monthly report tables below show what data you can expect in each `processingDate` and when you can expect to see complete data sets for a given date.

> **Note**: These are not fields in reports, but descriptions of what you might read in your reports.

These are not fields in reports, but descriptions of what you might read in your reports.

##### Daily Reports

| Processing date in API | Date column in report | Completed partition | What you can expect |
| --- | --- | --- | --- |
| 2024-04-01 | 2024-03-30 | 2024-03-30 | Full, complete data for events that happened on 3/30. |
| 2024-04-01 | 2024-03-31 | 2024-03-30 | Full, but not complete, data for events that happened on 3/31. |
| 2024-04-02 | 2024-03-31 | 2024-03-31 | Full, complete data for events that happened on 3/31. |
| 2024-04-02 | 2024-04-01 | 2024-03-31 | Full, but not complete, data for events that happened on 4/1. |
| 2024-04-03 | 2024-04-01 | 2024-04-01 | Full, complete data for events that happened on 4/1. |
| 2024-04-03 | 2024-04-02 | 2024-04-01 | Full, but not complete, data for events that happened on 4/2. |

##### Weekly Reports

| Processing date | Date column in report | Completed partition | What you can expect |
| --- | --- | --- | --- |
| 2024-04-05 | 2024-03-25 | 2024-03-25 | Full, complete data for events that happened in week 3/25–3/31. |
| 2024-04-12 | 2024-04-01 | 2024-04-01 | Full, complete data for events that happened in week 4/1–4/7. |

##### Monthly Reports

| Processing date | Date column in report | Completed partition | What you can expect |
| --- | --- | --- | --- |
| 2024-04-05 | 2024-03-01 | 2024-03-01 | Full, complete data for events that happened in the month of March. |
| 2024-05-05 | 2024-04-01 | 2024-04-01 | Full, complete data for events that happened in the month of April. |

## See Also

- [Protecting user privacy in report data](privacy.md)
  Understand measures that help protect user privacy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/data-completeness-corrections)*