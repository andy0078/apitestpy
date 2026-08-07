package api.buyer;

import core.BaseApi;
import io.restassured.response.Response;
import model.OrderRequest;

public class OrderApi extends BaseApi {

    public Response createOrder(OrderRequest request){
        return post("/order/create", request);
    }

    public Response queryOrder(String orderId){
        return get("/order/" + orderId);
    }
}
