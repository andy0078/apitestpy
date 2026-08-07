package core;

public class TokenManager {
    private static String token;

    public static String getToken(){
        if(token == null){
            login();
        }
        return token;
    }

    private static void login(){
        // TODO call login api and cache token
        token = "mock-token";
    }

    public static void refresh(){
        login();
    }
}
