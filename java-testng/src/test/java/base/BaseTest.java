package base;

import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;

public class BaseTest {

    @BeforeClass
    public void setUp(){
        System.out.println("init api test environment");
    }

    @AfterClass
    public void tearDown(){
        System.out.println("cleanup api test environment");
    }
}
