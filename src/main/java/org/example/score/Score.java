package org.example.score;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@Entity
@Table(name = "scores")
public class Score {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private String id;
    private Float toan;
    private Float nguVan;
    private Float ngoaiNgu;
    private Float vatLi;
    private Float hoaHoc;
    private Float sinhHoc;
    private Float lichSu;
    private Float diaLi;
    private Float gdcd;
    private String maNgoaiNgu;
    @CreationTimestamp
    private String createdAt;
    @UpdateTimestamp
    private String updatedAt;
}
