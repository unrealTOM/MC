# https://zhuanlan.zhihu.com/p/39253127

function walk(L=50)
    t = 2
    x = 2
    while x != 1
        if rand() < 0.5
            x += 1
        else
            x -= 1
        end 
        if x > L
            x = L
        end
        t += 1
    end
    return t
end

function run(L, N)
    times = Int64[]
    for i in 1:N
        push!(times, walk(L))
    end
    return times
end

function repeat(L, N, M)
    [mean(run(L, N)) for i in 1:M]
end

data = repeat(50, 1000, 10000);
using Plots
mean(data)
histogram(data)
