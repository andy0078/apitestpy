package testcase;

import api.basic.FileApi;
import base.BaseTest;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

public class FileTest extends BaseTest {

    private final FileApi fileApi = new FileApi();

    @Test
    public void uploadFileTest(){
        Response response = fileApi.uploadFile("data/test.png");
        Assert.assertEquals(response.statusCode(),200);
    }
}
