package com.ll.medium.domain.post.service;

import com.ll.medium.domain.post.dto.PostRequestDto;
import com.ll.medium.domain.post.entity.Post;
import com.ll.medium.domain.post.repository.PostRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class PostService {
    private final PostRepository postRepository;

    public void write(PostRequestDto postRequestDto, Integer memberId) {
        //1. PostController로부터 받아온 정보를 가지고 Post Entity에 담기
        Post post = new Post();
        post.setTitle(postRequestDto.getTitle());
        post.setBody(postRequestDto.getBody());
        post.setPublished(postRequestDto.isPublished());
        post.setMemberId(memberId);

        //2. Post Entity를 저장
        postRepository.save(post);
    }
}
