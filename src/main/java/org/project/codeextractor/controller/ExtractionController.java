package org.project.codeextractor.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/code")
@CrossOrigin(origins = "*") // allow requests from any frontend (can restrict later)
public class ExtractionController {

    @PostMapping("/extract")
    public ResponseEntity<String> extractCode(@RequestBody Map<String, String> request) {
        String youtubeUrl = request.get("youtubeUrl");

        if (youtubeUrl == null || youtubeUrl.isBlank()) {
            return ResponseEntity.badRequest().body("YouTube URL is required.");
        }

        System.out.println("Received YouTube URL: " + youtubeUrl);

        // Replace this block later with Python process call
        String dummyCode = """
                // Sample extracted code
                public class HelloWorld {
                    public static void main(String[] args) {
                        System.out.println("Hello, world!");
                    }
                }
                """;

        return ResponseEntity.ok(dummyCode);
    }

    @GetMapping("/status")
    public ResponseEntity<String> status() {
        return ResponseEntity.ok(" Code extraction service is up and running!");
    }
}
