# SovCondition

**Framework**: Apple Ads  
**Kind**: dictionary  
**Role**: Object

The list of condition objects that allow users to filter a list of records.

**Availability**:
- Search Ads 4.6+ - Deprecated in 5.2

> **Deprecated**: Apple Ads Campaign Management API is deprecated. Instead, use the [Apple Ads Platform API](../apple-ads-platform-api/apple-ads-platform-api.md).

## Declaration

```
object SovCondition
```

## Discussion

The `Condition` object functionality is similar to the `WHERE` clause in SQL.

## Properties

- `field` (string): A list of field names to return within each record.
- `operator` (string): The operator values compare attributes to a list of specified values.

  The `IN` operator matches any value in a list of specified values.

  **Allowed Values**: `IN`
- `values` ([string]): A list of matching values.

## See Also

### Impression Share Report Request and Response Objects
- [object CustomReportRequest](./customreportrequest.md)
  The Impression Share report request body.
- [object CustomReportResponse](./customreportresponse.md)
  A container for Impression Share report metrics.
- [object CustomReportResponseBody](./customreportresponsebody.md)
  A container for the Impression Share report response body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/sovcondition)*