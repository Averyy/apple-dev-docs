# App Store Reports Endpoints

**Framework**: Apple Ads Platform API  
**Role**: API Collection

Retrieve App Store performance metrics for campaigns, ad groups, ads, keywords, and search terms.

**Availability**:
- Apple Ads Platform API 1.0+

## Overview

All five endpoints share one `POST` query structure. Each request takes a `timeRange`, `filters`, and `sorting`, and returns rows with total and granular metrics. Ad group, ad, keyword, and search term reports require a `campaignId` filter.

For the shared request objects, see [Shared Objects](./reports-shared-objects.md). For the full reporting overview, see [Managing Reports](./reports.md).

## Topics

- [Campaigns Report](./get-app-campaign-reports.md)
  Retrieve performance metrics for campaigns.
- [Ad Groups Report](./get-app-ad-group-reports.md)
  Retrieve performance metrics for ad groups.
- [Ads Report](./get-app-ad-reports.md)
  Retrieve performance metrics for ads.
- [Keywords Report](./get-app-keyword-reports.md)
  Retrieve performance metrics for keywords.
- [Search Terms Report](./get-app-search-term-reports.md)
  Retrieve performance metrics for the actual search terms that triggered keyword matches.

## See Also

### Reports
- [Managing Reports](./reports.md)
  Retrieve performance data for campaigns, ad groups, ads, keywords, and search terms.
- [Brands Reports Endpoints](./brands-reports-endpoints.md)
  Retrieve performance data for Apple Maps campaigns, ad groups, ads, keywords, and search terms.
- [Apps Data Objects](./apps-reports-objects.md)
  Request, response, and metadata objects for Apps report endpoints.
- [Brands Data Objects](./brands-reports-objects.md)
  Explore the request, response, and metadata objects that Brands report endpoints use.
- [Shared Objects](./reports-shared-objects.md)
  Define time ranges, filters, sorting, and pagination for report requests, and read the shared metrics in responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/apps-reports-endpoints)*