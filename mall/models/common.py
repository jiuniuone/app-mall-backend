class Role:
    super_admin = 1000
    chocies = (
        (super_admin, "超级管理员"),
    )

    @classmethod
    def get_title(cls, role):
        return ",".join([item[1] for item in cls.chocies if item[0] == role])


class Gender:
    woman = 0
    man = 1
    chocies = (
        (woman, "女"),
        (man, "男"),
    )
