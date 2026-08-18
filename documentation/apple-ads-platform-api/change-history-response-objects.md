# Change History Response Objects

**Framework**: Apple Ads Platform API

Parse the audit summary and change detail objects returned by change history endpoints.

**Availability**:
- Apple Ads Platform API 1.0+

## Topics

- [object ActivityDetail](activitydetail.md)
  A group of field-level changes that occurred within a single activity context in a change details record.
- [object AuditSummary](auditsummary.md)
  One row in the query change history response, grouping a single actor’s entity changes in one transaction by entity type and event type.
- [object AuditSummaryResponse](auditsummaryresponse.md)
  The response envelope returned by the Query Change History endpoint, wrapping an array of audit summary rows with pagination metadata.
- [object BaseAuditResponse](baseauditresponse.md)
  Common response envelope fields shared by all change history response objects.
- [object ChangeDetails](changedetails.md)
  Field-level change record for a single API entity within a transaction.
- [object ChangeDetailsResponse](changedetailsresponse.md)
  The response envelope returned by the Get Change History Detail endpoint, wrapping an array of change detail records with pagination metadata.
- [object ErrorMessage](errormessage.md)
  Error information returned in a change history response when a request fails.

## See Also

- [Change History Endpoints](change-history-endpoints.md)
  Query audit summaries and retrieve change detail records for entities in an ad account.
- [Change History Query Objects](change-history-query-objects.md)
  Build the filter, sort, and pagination inputs for change history query requests.
- [Change History Enumerations](change-history-enumerations.md)
  Look up the enumerated values accepted in change history query and response fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/change-history-response-objects)*