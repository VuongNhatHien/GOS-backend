package org.example.score;

import lombok.RequiredArgsConstructor;
import org.example.shared.BadRequestException;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ScoreService {
    private final ScoreRepository scoreRepository;

    public Score findScoreByUserId(String userId) {
        return scoreRepository.findById(userId).orElseThrow(() -> new BadRequestException("USER_NOT_FOUND"));
    }
}
