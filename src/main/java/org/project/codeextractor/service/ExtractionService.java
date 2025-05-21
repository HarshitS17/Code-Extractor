package org.project.codeextractor.service;

import org.springframework.stereotype.Service;// this is to make this file as service

import java.io.IOException;// to handle the i/o errors
import java.io.InputStreamReader;// scripts k output read krne k liye/ ya mtlb streams smbhaalne k liye
import java.io.BufferedReader;// script k output ko line by line pdhne k liye

@Service
public class ExtractionService {

    public String runPython(String youtubeUrl) {
        try {
            ProcessBuilder pb = new ProcessBuilder(
                    "python3", // or "python3" depending on your system
                    "scripts/extract_code.py", // relative path to your Python script
                    youtubeUrl
            );
            pb.redirectErrorStream(true);//Combine stdout or stderr of the pyScript

            Process process = pb.start(); // start the python script

            // Reader to capture output from the script
            BufferedReader br = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder output = new StringBuilder();
            String line;

            while ((line = br.readLine()) != null) {
                output.append(line).append("\n"); // Append each line to the result
            }

            int exitCode = process.waitFor(); // Wait until script finishes

            if (exitCode == 0) {
                return output.toString(); // Return full output from Python
            } else {
                return "Python script failed with exit code: " + exitCode;
            }

        } catch (IOException | InterruptedException e) {
            return "Error running python script" + e.getMessage();
        }
    }

    public String extractCodeFromYoutubeUrl(String youtubeUrl) {
        //  a dummy message to test functionality
        return "Code extracted from URL: " + youtubeUrl;
    }
}
