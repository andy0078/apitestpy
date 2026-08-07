package core;

import io.restassured.response.Response;

import static io.restassured.RestAssured.given;

public class BaseApi {

    protected String host = "https://test.example.com";

    protected Response get(String path){
        return given()
                .header("Authorization", TokenManager.getToken())
                .when()
                .get(host + path);
    }

    protected Response post(String path,Object body){
        return given()
                .header("Authorization", TokenManager.getToken())
                .contentType("application/json")
                .body(body)
                .when()
                .post(host + path);
    }

    protected Response upload(String path,String file){
        return given()
                .header("Authorization", TokenManager.getToken())
                .multiPart("file",file)
                .post(host + path);
    }
}