# AuditQuery.Options

**Framework**: Apple Ads Platform API  
**Kind**: dictionary

A flat key-value map of additional query controls.

**Availability**:
- apple-ads-platform-api 1.0+

## Declaration

```swift
object AuditQuery.Options
```

#### Discussion

`options` has three well-known keys (`needTotals`, `timeZone`, and `metadata`), each with a fixed set of accepted string values and a default. The API accepts any other key as a plain string (labeled `Any Key` on the reference page) and passes it through without affecting the query.

All keys and values in `options` are strings: pass `needTotals` as `"true"` or `"false"`, not as a boolean, and `metadata` as `"none"`, `"latest"`, or `"snapshot"`.

## Properties

- `needTotals` (string): Skip the COUNT query when set to `false`, so `pagination.totalCount` returns `0` instead of the full result count. Accepted values: `true`, `false`. Default: `true`.
- `timeZone` (string): Controls how the API interprets `eventTime` filter values. `UTC` treats values as UTC. `ORTZ` interprets values in the org’s configured timezone and converts them to UTC server-side. Accepted values: `UTC`, `ORTZ`.
- `metadata` (string): Controls entity metadata included in change detail responses. `none` returns no metadata, `latest` joins current entity metadata, `snapshot` uses metadata captured at the time of the event. Accepted values: `none`, `latest`, `snapshot`. Default: `none`.
- `Any Key` (string): The API accepts any key other than `needTotals`, `timeZone`, or `metadata` as an arbitrary string value, but it has no effect on query behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/auditquery/options-data.dictionary)*