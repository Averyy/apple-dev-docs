# DestinationCreate.DestinationType

**Framework**: Apple Ads Platform API  
**Kind**: typealias  
**Role**: Type

The type of post-tap destination to create.

**Availability**:
- Apple Ads Platform API 1.0+

## Declaration

```
string DestinationCreate.DestinationType
```

## Possible Values

- `APP_STORE_PRODUCT_PAGE`: Directs users to the app’s product page in the App Store. Used with `DEFAULT_PRODUCT_PAGE` and `CUSTOM_PRODUCT_PAGE` creative types.
- `LOCAL_ADS_PLACECARD`: Directs users to the brand’s Maps place card. The only supported destination for Apple Maps ad creatives.

## Discussion

Apple Maps ad creatives only support `LOCAL_ADS_PLACECARD`, while App Store ad creatives use `APP_STORE_PRODUCT_PAGE`.

### Example

```json
{
  "destinationType": "APP_STORE_PRODUCT_PAGE"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-ads-platform-api/destinationcreate/destinationtype-data.typealias)*