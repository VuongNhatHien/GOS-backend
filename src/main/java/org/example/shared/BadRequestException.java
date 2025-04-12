package org.example.shared;

public class BadRequestException extends AppException {
    public BadRequestException(String code) {
        super(400, code);
    }
}
