package org.example.score;

import lombok.AllArgsConstructor;
import org.example.shared.ApiResponse;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("scores")
@RestController
@AllArgsConstructor
public class ScoreController {
    private final ScoreService scoreService;
    @GetMapping("/{userId}")
    public ApiResponse<Score> getScore(@PathVariable("userId") String userId) {
        return new ApiResponse<>(scoreService.findScoreByUserId(userId));
    }
}
