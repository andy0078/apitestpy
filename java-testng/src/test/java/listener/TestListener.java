package listener;

import org.testng.ITestListener;
import org.testng.ITestResult;

public class TestListener implements ITestListener {

    @Override
    public void onTestFailure(ITestResult result){
        System.out.println("Test failed: " + result.getName());
        System.out.println("collect api logs");
    }
}
