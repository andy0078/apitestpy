package model;

public class OrderRequest {
    private Integer userId;
    private Integer skuId;
    private Integer count;

    public Integer getUserId(){ return userId; }
    public void setUserId(Integer userId){ this.userId=userId; }

    public Integer getSkuId(){ return skuId; }
    public void setSkuId(Integer skuId){ this.skuId=skuId; }

    public Integer getCount(){ return count; }
    public void setCount(Integer count){ this.count=count; }
}
