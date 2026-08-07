package data;

import org.testng.annotations.DataProvider;

public class TestDataProvider {

    @DataProvider(name="orderData")
    public Object[][] orderData(){
        return new Object[][]{
            {1001,2001,1},
            {1002,2002,2}
        };
    }
}
