package org.project.codeextractor.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/code")
public class ExtractionController {

    @PostMapping("/extract")
    public ResponseEntity<String> extractCode(@RequestParam String youtubeUrl) {
        System.out.println("Received YouTube URL: " + youtubeUrl);

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
        return ResponseEntity.ok("Code extraction service is up and running!");
    }
}
