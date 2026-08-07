package api.basic;

import core.BaseApi;
import io.restassured.response.Response;

public class FileApi extends BaseApi {

    public Response uploadFile(String filePath){
        return upload("/uploaders", filePath);
    }
}
