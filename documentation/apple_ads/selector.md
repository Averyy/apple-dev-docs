# Selector

**Framework**: Apple Ads  
**Kind**: dictionary

The selector objects available to filter returned data.

**Availability**:
- Search Ads 2.0+

## Declaration

```swift
object Selector
```

#### Discussion

[`Selector`](selector.md) objects define what data the API returns when fetching resources. You use [`Selector`](selector.md) objects with find calls and reporting endpoints.

|  |  |
| --- | --- |
| Filtering | Specifies the criteria to filter the resources that return. |
| Sorting | Specifies the criteria to order the resources that return. |
| Paginating | Specifies the page segment of resources that return. |

The following is an example of using selectors to filter returned records:

```console
POST https://api.searchads.apple.com/api/v5/campaigns/find

{  
  "fields": [
    "id",
    "name",
    "adamId",
    "budgetAmount",
    "dailyBudgetAmount",
    "status",
    "servingStatus"
  ],
  "conditions": [
    {
      "field": "servingStatus",
      "operator": "IN",
      "values": [
        "NOT_RUNNING"
      ]
    }
  ],
  "orderBy": [
    {
      "field": "id",
      "sortOrder": "DESCENDING"
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 10
  }
}

```

You can also use [`Selector`](selector.md) objects to find archived or soft-deleted campaigns. By default, API fetch calls don’t return deleted resources, with the exception of GET by `a` resource `Id`. To retrieve deleted resources, you must explicitly request the call using the selector [`Condition`](condition.md).

The following example returns both deleted and undeleted resources:

```json
{
  "fields": null,
  "conditions": [
    {
      "field": "deleted",
      "operator": "IN",
      "values": [
        true,
        false
      ]
    }
  ],
  "orderBy": [
    {
      "field": "name",
      "sortOrder": "ASCENDING"
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 100
  }
}

```

## See Also

- [object Condition](condition.md)
  The list of condition objects that allow users to filter a list of records.
- [object PageDetail](pagedetail.md)
  The number of items that return in the page.
- [object Pagination](pagination.md)
  The procedure to refine returned results using limit and offset parameters.
- [object Sorting](sorting.md)
  The order of grouped results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple_ads/selector)*